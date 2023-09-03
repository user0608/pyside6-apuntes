from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar
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
        self.setWindowIcon(QIcon(ensurePath("gato.jpg")))

        # self.setStatusBar(QStatusBar(self)) # actiba los estatus tip

        menubar = self.menuBar()
        menu = menubar.addMenu("&Menu")
        menu.addAction("&Prueba")

        submenu = menu.addMenu("&Submenu")
        submenu.addAction("Accion 1")
        submenu.addAction("Accion 2")
        menu.addSeparator()

        menu.addAction(QIcon(ensurePath("exit.png")), "Exit", self.close)

        menu_ayuda = menubar.addMenu('Ayuda')
        action_info = QAction(
            QIcon(ensurePath("gato.jpg")), "Informacion", self)
        action_info.setShortcut("ctrl+i")
        action_info.triggered.connect(self.mostrar_info)

        # es nesesario self.setStatusBar(QStatusBar(self)
        action_info.setStatusTip("muestra informacion")

        menu_ayuda.addAction(action_info)

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
