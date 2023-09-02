import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class CustomColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        self.baselayout = QVBoxLayout()
        self.baselayout.addWidget(CustomColorBox("green"))
        self.baselayout.addWidget(CustomColorBox("red"))
        self.baselayout.addWidget(CustomColorBox("blue"))
        self.baselayout.addWidget(CustomColorBox("purple"))
        self.baselayout.addWidget(CustomColorBox("black"))

        self.baselayout.setContentsMargins(0, 0, 0, 0)
        self.baselayout.setSpacing(0)  # space beetwin widgets

        self.basewidget = QWidget()
        self.basewidget.setLayout(self.baselayout)

        self.setCentralWidget(self.basewidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
