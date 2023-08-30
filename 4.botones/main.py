from PySide6.QtWidgets import QApplication,  QPushButton, QMainWindow
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.button = QPushButton("Tocame")
        self.setCentralWidget(self.button)
        # self.button.clicked.connect(self.on_button_click)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_button_toggle)

        self.button.pressed.connect(self.on_button_pressed)
        self.button.released.connect(self.on_button_released)

        self.setWindowTitle("Hola Mundo")
        self.setMinimumSize(QSize(620, 480))
        self.setMaximumSize(QSize(820, 580))
        # self.setFixedSize(QSize(820, 580)) # no redimensionale

    def on_button_click(self):
        print("Hola como estas")

    def on_button_pressed(self):
        print("pressed!")

    def on_button_released(self):
        print("released!")

    def on_button_toggle(self, value):
        if value:
            self.button.setText("Hola, Etoy Activo")
        else:
            self.button.setText("Hi, No estoy")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
