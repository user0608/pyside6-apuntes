import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,  QWidget, QGridLayout


class ColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        grid.addWidget(ColorBox("orange"), 0, 0)
        grid.addWidget(ColorBox("purple"), 1, 1)
        grid.addWidget(ColorBox("magenta"), 2, 2)
        grid.addWidget(ColorBox("gray"), 2, 0)
        grid.addWidget(ColorBox("red"), 0, 0)
        grid.addWidget(ColorBox("cyan"), 0, 1)

        self.mainwidget = QWidget()
        self.mainwidget.setLayout(grid)

        self.setCentralWidget(self.mainwidget)
        self.resize(620, 480)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
