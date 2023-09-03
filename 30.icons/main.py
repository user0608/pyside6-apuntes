from PySide6.QtWidgets import QApplication,  QPushButton, QMainWindow, QStyle
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton)
        self.button = QPushButton(icon, "Guardar")
        self.setCentralWidget(self.button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
