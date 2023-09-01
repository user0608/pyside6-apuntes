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
        self.text.returnPressed.connect(self.on_enter)
        self.setCentralWidget(self.text)

        self.setMinimumSize(QSize(380, 220))

    def on_text_change(self, value):
        self.setWindowTitle(value)

    def on_enter(self):
        print(self.text.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
