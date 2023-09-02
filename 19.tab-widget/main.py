import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,  QTabWidget


class ColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        tabs = QTabWidget()

        tabs.addTab(ColorBox("orange"), "Naranja")
        tabs.addTab(ColorBox("green"), "Verder")
        tabs.addTab(ColorBox("purple"), "Morado")
        tabs.addTab(ColorBox("red"), "Rojo")
        tabs.addTab(ColorBox("magenta"), "Magenta")

        # tabs.setTabPosition(QTabWidget.TabPosition.North)
        # tabs.setTabPosition(QTabWidget.TabPosition.South)
        # tabs.setTabPosition(QTabWidget.TabPosition.East)
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True) # puede cambiar de posicion

        self.setCentralWidget(tabs)
        self.resize(620, 480)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
