from PySide6.QtWidgets import QApplication,   QMainWindow, QComboBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.combo = QComboBox()
        self.combo.addItems(["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"])
        self.combo.currentIndexChanged.connect(self.on_index_change)
        self.combo.currentTextChanged.connect(self.on_text_change)
        self.setCentralWidget(self.combo)

    def on_index_change(self, index):
        print(index)

    def on_text_change(self, value):
        print(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
