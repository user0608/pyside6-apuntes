from PySide6.QtWidgets import QApplication,   QMainWindow, QLabel
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.lable = QLabel("Soy una etiqueta")
        self.lable.setFont(QFont("Comic Sans MS", 24))
        self.lable.setPixmap(QPixmap("6.labels/gato.jpg"))
        self.lable.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.lable)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
