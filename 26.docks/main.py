from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar, QLabel, QDockWidget
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QTranslator, QLibraryInfo, Qt
from pathlib import Path
import sys


class ColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


def ensurePath(path: str) -> str:
    return f"{Path(__file__).parent.absolute()}/{path}"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Python")
        self.initialize()
        self.build_docks()

    def build_docks(self):
        dock1 = QDockWidget()

        dock1.setWidget(ColorBox("blue"))
        dock1.setMinimumWidth(120)
        dock1.setMinimumHeight(50)
        dock1.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures |
                          #  QDockWidget.DockWidgetFeature.DockWidgetFloatable |
                          QDockWidget.DockWidgetFeature.DockWidgetMovable)
        dock1.setWindowTitle("Dock 1")

        dock2 = QDockWidget()

        dock2.setWidget(ColorBox("green"))
        dock2.setMinimumWidth(120)
        dock2.setMinimumHeight(50)
        dock2.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures |
                          QDockWidget.DockWidgetFeature.DockWidgetMovable)
        dock2.setWindowTitle("Dock 2")

        dock3 = QDockWidget()
        dock3.setWidget(ColorBox("red"))
        dock3.setMinimumWidth(120)
        dock3.setMinimumHeight(50)
        dock3.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures |
                          QDockWidget.DockWidgetFeature.DockWidgetMovable)
        dock3.setWindowTitle("Dock 3")

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock1)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock2)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock3)

        self.setCentralWidget(ColorBox("gray"))

        pass

    def initialize(self):
        self.resize(480, 320)
        self.setWindowIcon(QIcon(ensurePath("cat.png")))
        self.setStatusBar(QStatusBar(self))

        tools = QToolBar("Tool Bar")
        action_info = QAction(
            QIcon(ensurePath("cat.png")), "Informacion", self)

        action_info.setShortcut("ctrl+i")
        action_info.setToolTip("Informacion")

        action_info.triggered.connect(self.mostrar_info)

        tools.addAction(action_info)
        tools.addAction(QIcon(ensurePath("exit.png")), "Salir", self.close)

        self.addToolBar(tools)

    def mostrar_info(self):
        QMessageBox.information(self, "Informacion",
                                "Esto es un texto informativo")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    traductor = QTranslator(app)

    traducciones = QLibraryInfo.path(
        QLibraryInfo.LibraryPath.TranslationsPath)
    traductor.load("qt_es", traducciones)

    app.installTranslator(traductor)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
