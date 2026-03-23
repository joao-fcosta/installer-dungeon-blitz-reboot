from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor
from PySide6.QtCore import Qt

class OutlinedLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.outline_color = QColor(0, 0, 0)
        self.outline_width = 3

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        path = QPainterPath()
        metrics = painter.fontMetrics()
        # Centralização precisa do texto dentro do Label
        text_width = metrics.horizontalAdvance(self.text())
        x = (self.width() - text_width) / 2
        y = (self.height() + metrics.ascent() - metrics.descent()) / 2
        
        path.addText(x, y, self.font(), self.text())

        # Desenha a borda preta
        pen = QPen(self.outline_color)
        pen.setWidth(self.outline_width)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawPath(path)

        # Preenche com branco
        painter.fillPath(path, QColor(255, 255, 255))