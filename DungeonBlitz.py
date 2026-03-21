import tkinter as tk
from tkinter import ttk
import threading
import time
import os
import sys
from PIL import Image, ImageTk
from core.installer import is_installed, install
from core.server_manager import ServerManager
from core.launcher import start_game
from core.updater import check_for_updates

class DungeonBlitzLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        
        self.width = 800
        self.height = 600
        self.root.overrideredirect(False)
        self._center_window()

        try:
            bg_image = Image.open("image/background.png")
            bg_image = bg_image.resize((self.width, self.height), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Erro ao carregar fundo: {e}")
            self.root.configure(bg="#2c3e50") # Fundo sólido de segurança

        box_img = Image.open("init.png")
        box_img = box_img.resize((400, 200), Image.Resampling.LANCZOS)
        self.box_photo = ImageTk.PhotoImage(box_img)

        self.center_frame = tk.Label(self.root, image=self.box_photo, bg="#1a1a1a", bd=0)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=200)

        # 4. Texto de Status Customizado
        self.status_label = tk.Label(
            self.center_frame, 
            text="Iniciando...", 
            fg="#f1c40f",
            bg="#1a1a1a",
            font=("Verdana", 12, "bold")
        )
        self.status_label.pack(pady=30)

        # 5. Barra de Progresso Customizada (Inspirado nas cores do logo)
        # Criando um estilo customizado para a barra
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure(
            "Game.Horizontal.TProgressbar", 
            troughcolor='#2c3e50', # Cor do fundo da barra
            background='#e67e22',   # Laranja vibrante do logo
            thickness=20
        )

        self.progress = ttk.Progressbar(
            self.center_frame, 
            style="Game.Horizontal.TProgressbar", 
            orient="horizontal", 
            length=350, 
            mode="determinate"
        )
        self.progress.pack(pady=10)

        # 6. Botão de Fechar (Discreto, no canto superior direito)
        self.close_btn = tk.Label(
            self.root, 
            text="[X]", 
            fg="#95a5a6", 
            bg="#2c3e50", 
            font=("Arial", 10)
        )
        self.close_btn.place(x=self.width-30, y=10)
        self.close_btn.bind("<Button-1>", lambda e: self.root.destroy())

        # 7. Iniciar o processo lógico em Background
        self.update_thread = threading.Thread(target=self.run_launcher_logic)
        self.update_thread.start()

    def _center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f'{self.width}x{self.height}+{int(x)}+{int(y)}')

    def update_status(self, text, progress_val=None):
        """Função segura para atualizar a UI a partir do thread de lógica."""
        self.root.after(0, lambda: self._update_ui(text, progress_val))

    def _update_ui(self, text, progress_val):
        self.status_label.config(text=text)
        if progress_val is not None:
            self.progress['value'] = progress_val

    def run_launcher_logic(self):
        try:
            if not is_installed():
                self.update_status("Primeira instalação... Isso pode demorar.", 20)
                install()
            
            self.update_status("Buscando atualizações...", 50)
            check_for_updates()
            
            self.update_status("Iniciando servidor local...", 80)
            manager = ServerManager()
            server_process = manager.start()
            
            if not server_process:
                self.update_status("❌ Falha ao iniciar servidor!", 0)
                time.sleep(3)
                self.root.after(0, self.root.destroy)
                return

            self.update_status("🎮 Jogo iniciado! Divirta-se.", 100)
            # self.root.after(0, self.root.withdraw) 

            flash = start_game()

            if flash:
                # O código para aqui até o jogador fechar a janela do Flash
                flash.wait()

            # 5. Finalização
            if server_process:
                print("Encerrando servidor...")
                server_process.terminate()

            print("Saindo...")
            self.root.after(0, self.root.destroy)

        except Exception as e:
            self.update_status(f"❌ Erro Crítico: {e}", 0)
            print(f"Erro: {e}")
            time.sleep(5)
            self.root.after(0, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = DungeonBlitzLauncher(root)
    root.mainloop()
