from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
import sys


class SubWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.resize(480, 320)
        self.setWindowTitle("SubVentana")
        label = QLabel("Soy una etiqueta")

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.subventana = SubWindows()
        self.initialize()

    def initialize(self):
        self.resize(480, 320)
        self.setWindowTitle("Ventana Principal")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        button = QPushButton("SubVentana")
        button.clicked.connect(self.on_click)

        self.hide_button = QPushButton("Ocultar sub ventana")
        self.hide_button.clicked.connect(self.on_hide)
        self.hide_button.setVisible(False)

        layout.addWidget(button)
        layout.addWidget(self.hide_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_click(self):
        self.hide_button.setVisible(True)
        self.subventana.show()

    def on_hide(self):
        self.subventana.hide()
        self.hide_button.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
