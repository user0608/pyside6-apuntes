from PySide6.QtWidgets import QApplication,  QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QInputDialog, QFontDialog, QColorDialog

from PySide6.QtCore import QTranslator, QLibraryInfo, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        open_file_dialog = QPushButton("Open File")
        open_file_dialog.clicked.connect(self.on_open_file)
        layout.addWidget(open_file_dialog)

        save_file_dialog = QPushButton("Save File")
        save_file_dialog.clicked.connect(self.on_save_file)
        layout.addWidget(save_file_dialog)

        text_dialog = QPushButton("Text")
        text_dialog.clicked.connect(self.on_text)
        layout.addWidget(text_dialog)

        numero_dialog = QPushButton("Numero")
        numero_dialog.clicked.connect(self.on_numero)
        layout.addWidget(numero_dialog)

        decimal_dialog = QPushButton("Double")
        decimal_dialog.clicked.connect(self.on_decimal_numero)
        layout.addWidget(decimal_dialog)

        items_dialog = QPushButton("Items")
        items_dialog.clicked.connect(self.on_items)
        layout.addWidget(items_dialog)

        self.fuente_dialog = QPushButton("Fonts")
        self.fuente_dialog.clicked.connect(self.on_fuente)
        layout.addWidget(self.fuente_dialog)

        self.color_dialgo = QPushButton("Color")
        self.color_dialgo.clicked.connect(self.on_color)
        layout.addWidget(self.color_dialgo)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        self.resize(580, 380)

    def on_open_file(self):
        # file, _ = QFileDialog.getOpenFileName(self)
        file, info = QFileDialog.getOpenFileName(self)
        print(info)
        print(file)

    def on_save_file(self):
        file, info = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
        print(info)
        print(file)

    def on_text(self):
        texto, ok = QInputDialog.getText(self, "Titulo", "Nombre completo")
        if ok:
            print(texto)

    def on_numero(self):
        num, ok = QInputDialog.getInt(self, "Titulo", "Numero")
        if ok:
            print(num)

    def on_decimal_numero(self):
        num, ok = QInputDialog.getDouble(self, "Titulo", "Numero")
        if ok:
            print(num)

    def on_items(self):
        color, ok = QInputDialog.getItem(self, "Titulo", "Colores", [
            "Rojo", "Azul", "Verde", "Blanco"], editable=False)
        if ok:
            print(color)

    def on_fuente(self):
        ok, font = QFontDialog.getFont(self)
        if ok:
            self.fuente_dialog.setFont(font)

    def on_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_dialgo.setStyleSheet(f"background-color:{color.name()}")


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
