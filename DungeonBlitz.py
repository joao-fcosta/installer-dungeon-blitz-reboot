import sys
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread, Signal
from ui.launcher_gui import LauncherWindow
from core.installer import is_installed, install
from core.server_manager import ServerManager
from core.launcher import start_game
from core.updater import check_for_updates
from core.utils import ConsoleRedirector

# 1. Criamos uma classe de Worker para rodar a lógica sem travar a interface
class GameLogicWorker(QThread):
    # Sinais para enviar dados da thread de lógica para a interface
    status_updated = Signal(str, int)  # Envia (Texto, Porcentagem)
    finished = Signal()

    def run(self):
        try:
            if not is_installed():
                self.status_updated.emit("Primeira instalação... Isso pode demorar.", 20)
                install()
            
            self.status_updated.emit("Buscando atualizações...", 50)
            check_for_updates()
            
            self.status_updated.emit("Iniciando servidor local...", 80)
            manager = ServerManager()
            server_process = manager.start()
            
            if not server_process:
                self.status_updated.emit("Falha ao iniciar servidor!", 0)
                time.sleep(3)
                self.finished.emit()
                return

            self.status_updated.emit("Jogo iniciado! Divirta-se.", 100)
            flash = start_game()

            if flash:
                flash.wait()

            if server_process:
                print("Encerrando servidor...")
                server_process.terminate()
            
            self.finished.emit()

        except Exception as e:
            self.status_updated.emit(f"Erro Crítico: {e}", 0)
            time.sleep(5)
            self.finished.emit()

class LauncherController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.gui = LauncherWindow()
        
        sys.stdout = ConsoleRedirector(self.safe_update_from_console)
        
        self.worker = GameLogicWorker()
        self.worker.status_updated.connect(self.gui.update_status)
        self.worker.finished.connect(self.gui.close)
        
        self.gui.show()
        self.worker.start()
        
        sys.exit(self.app.exec())

    def safe_update_from_console(self, text):
        self.gui.update_status(text)

if __name__ == "__main__":
    LauncherController()