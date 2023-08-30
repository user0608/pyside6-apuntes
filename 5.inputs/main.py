from PySide6.QtWidgets import QApplication,   QMainWindow, QLineEdit
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Hola Mundo")

        self.text = QLineEdit()
        self.text.textChanged.connect(self.on_text_change)

        self.setCentralWidget(self.text)

        self.setMinimumSize(QSize(380, 220))

    def on_text_change(self, value):
        self.setWindowTitle(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
