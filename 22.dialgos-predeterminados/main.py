from PySide6.QtWidgets import QApplication,  QMainWindow, QPushButton, QMessageBox
from PySide6.QtGui import QIcon
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
        self.setWindowIcon(QIcon(ensurePath("gato.jpg")))
        self.button = QPushButton("Show Dialog")
        self.button.clicked.connect(self.on_click)

        self.setCentralWidget(self.button)
        self.resize(480, 320)

    def on_click(self):
        # respuesta = QMessageBox.question(
        #     self, "Pregunta", "Mensaje del dialgo")
        # QMessageBox.about(
        #     self,
        #     "Acerca de", "Informacion del programa\nOtros parrafo"
        # )
        buttons = QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel
        message = "Esta seguro de aplicar los cambios?"
        result = QMessageBox.warning(self, "Aviso", message, buttons=buttons)
        print(result)
        if result == QMessageBox.StandardButton.Apply:
            print("Aplicar los cambios")


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
