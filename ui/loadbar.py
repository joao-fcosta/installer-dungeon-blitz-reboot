from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class CustomProgressBar(QLabel):
    def __init__(self, folder_path):
        super().__init__()
        self.frames = []
        # Importante: Permitir transparência no widget da barra
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent; border: none;")
        
        for i in range(1, 101):
            pix = QPixmap(f"{folder_path}/{i}.png")
            self.frames.append(pix)
            
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if self.frames:
            self.setPixmap(self.frames[0])

    def update_progress(self, progress_percent):
        if not self.frames: return
        idx = int((progress_percent / 100) * (len(self.frames) - 1))
        idx = max(0, min(len(self.frames) - 1, idx))
        self.setPixmap(self.frames[idx])