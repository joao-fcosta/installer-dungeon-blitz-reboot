import os
from PySide6.QtWidgets import QWidget, QLabel, QFrame
from PySide6.QtGui import QPixmap, QFont, QFontDatabase, QIcon
from PySide6.QtCore import Qt
from ui.loadbar import CustomProgressBar
from ui.outlined_label import OutlinedLabel

class LauncherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. Configurações de Identidade
        self.setWindowTitle("Dungeon Blitz Launcher")
        self.setWindowIcon(QIcon("image/icon.ico"))

        # 2. Carregar a imagem de fundo PRIMEIRO para decidir o tamanho
        self.bg_pixmap = QPixmap("image/background.png")
        self.setFixedSize(909, 600)

        # 3. Carregar Fonte
        font_path = "font/Helvetica.otf"
        font_id = QFontDatabase.addApplicationFont(font_path)
        self.custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0] if font_id != -1 else "Arial"

        # 4. Inicializar a barra (618x64)
        self.custom_bar = CustomProgressBar("image/loadbar")
        self.custom_bar.setFixedSize(618, 64)

        # 5. Montar os widgets
        self._setup_ui()
        
        # Centraliza a janela na tela
        self._center_on_screen()

    def _center_on_screen(self):
        """Centraliza a janela independente da resolução do monitor."""
        screen = self.screen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def _setup_ui(self):
        # Background fixo (sem esticar, qualidade máxima)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(self.bg_pixmap)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        # Footer (Container da barra)
        self.footer = QFrame(self)
        self.footer.setStyleSheet("background: transparent; border: none;")
        self.footer.setFixedSize(618, 80)
        
        # Posiciona a barra dentro do footer
        self.custom_bar.setParent(self.footer)
        self.custom_bar.move(0, 0)

        # Texto com Borda (OutlinedLabel)
        self.status_label = OutlinedLabel("Iniciando...", self.footer)
        self.status_label.setFont(QFont(self.custom_font_family, 11, QFont.Weight.Bold))
        # Ajustado para ficar sobre a barra
        self.status_label.setGeometry(0, -10, 618, 40) 

        # Posicionamento do footer (sempre relativo ao fundo)
        self._position_elements()

    def _position_elements(self):
        # Centraliza a barra horizontalmente
        x = (self.width() - 618) // 2
        # Posiciona a 85% da altura da imagem de fundo
        y = int(self.height() * 0.85)
        self.footer.move(x, y)

    def update_status(self, text, progress_val=None):
        self.status_label.setText(text)
        self.status_label.update()
        if progress_val is not None:
            self.custom_bar.update_progress(int(progress_val))