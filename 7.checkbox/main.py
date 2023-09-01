from PySide6.QtWidgets import QApplication,   QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.checkbox = QCheckBox("Activar verificacion")
        self.checkbox.stateChanged.connect(self.on_chanage)
        self.setCentralWidget(self.checkbox)

    def on_chanage(self, value):
        if value == 2:
            print("Esta marcado")
        else:
            print("No esta marcado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
