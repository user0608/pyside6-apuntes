from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QTranslator, QLibraryInfo
from pathlib import Path
import sys


def ensurePath(path: str) -> str:
    return f"{Path(__file__).parent.absolute()}/{path}"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.resize(480, 320)
        self.setWindowIcon(QIcon(ensurePath("cat.png")))
        self.setStatusBar(QStatusBar(self))

        tools = QToolBar("Tool Bar")
        tools.addAction(QIcon(ensurePath("exit.png")), "Salir", self.close)

        action_info = QAction(
            QIcon(ensurePath("cat.png")), "Informacion", self)
        action_info.setShortcut("ctrl+i")
        action_info.setToolTip("Informacion")
        action_info.triggered.connect(self.mostrar_info)

        tools.addAction(action_info)
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
