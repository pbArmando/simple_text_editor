from PySide6.QtGui import QAction, QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit, QFileDialog, QMessageBox, QDockWidget
import sys

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toma notas")
        self.resize(800, 600)
        self.ruta_actual = None

        # Iniciamos el editor
        self.editor = QPlainTextEdit()
        fuente = QFont("Arial", 12)
        self.editor.setFont(fuente)
        self.editor.setStyleSheet("""
            QPlainTextEdit {
                background-color: #000000;
                color: #00ff00;
                border: none;
            }
        """)
        self.menuBar().setStyleSheet("""
            QMenuBar {
                background-color: #000000;
                color: #00ff00;
                border: none;
            }
            QMenuBar::item {
                padding: 5px 10px;
            }
            QMenuBar::item:selected {
                background-color: #003300;
                color: #00ff00;
            }
            QMenu {
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #008800;
            }
            QMenu::item {
                padding: 5px 25px;
                min-width: 150px;
            }
            QMenu::item:selected {
                background-color: #003300;
                color: #00ff00;
            }
            QMenu::separator {
                height: 1px;
                background-color: #008800;
                margin: 5px 0;
            }
        """)
        self.statusBar().setStyleSheet("""
            QStatusBar {
                background-color: #000000;
                color: #00ff00;
                border-top: 1px solid #008800;
            }
        """)
        
        self.statusBar().showMessage("Automatas II")
        self.setCentralWidget(self.editor)
        self.crear_menu()

    def crear_menu(self):
        menu_bar = self.menuBar()
        menu_archivo = menu_bar.addMenu("Archivo")
        
        action_nuevo = QAction("Nuevo", self)
        action_nuevo.setShortcut("Ctrl+N")
        action_nuevo.triggered.connect(self.nuevo)
        menu_archivo.addAction(action_nuevo)

        action_abrir = QAction("Abrir", self)
        action_abrir.setShortcut("Ctrl+O")
        action_abrir.triggered.connect(self.abrir)
        menu_archivo.addAction(action_abrir)

        action_guardar = QAction("Guardar", self)
        action_guardar.setShortcut("Ctrl+S")
        action_guardar.triggered.connect(self.guardar)
        menu_archivo.addAction(action_guardar)

        action_guardar_como = QAction("Guardar como", self)
        action_guardar_como.setShortcut("Ctrl+Shift+S")
        action_guardar_como.triggered.connect(self.guardar_como)
        menu_archivo.addAction(action_guardar_como)

        action_salir = QAction("Salir", self)
        action_salir.setShortcut("Ctrl+Q")
        action_salir.triggered.connect(self.salir)
        menu_archivo.addAction(action_salir)

        action_limpiar = QAction("Limpiar", self)

    def nuevo(self):
        self.editor.clear()
        self.setWindowTitle("Nuevo archivo")

    def abrir(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        if ruta:
            try:
                with open (ruta, "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                self.editor.setPlainText(contenido)
                self.ruta_actual = ruta
                self.setWindowTitle(f"Toma notas - {ruta}")
                self.statusBar().showMessage("Archivo abierto correctamente")
            except Exception as e:
                self.statusBar().showMessage(f"Error al abrir: {e}")
        

    def guardar(self):
        if self.ruta_actual is None:
            self.guardar_como()
        else:
            self._escribir_archivo(self.ruta_actual)

    def guardar_como(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        if ruta:
            self._escribir_archivo(ruta)

    def salir(self):
        self.close()

    def closeEvent(self, event):
        if self.editor.document().isModified():
            resp = QMessageBox.question(self, "Salir", "¿Deseas guardar los cambios?")
            if resp == QMessageBox.Yes:
                self.guardar_como()
                event.accept()
            else:
               event.accept()
            
    def _escribir_archivo(self, ruta):
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(self.editor.toPlainText())
            self.ruta_actual = ruta
            self.setWindowTitle(f"Toma notas - {ruta}")
            self.statusBar().showMessage("Archivo guardado")
        except Exception as e:
            self.statusBar().showMessage(f"Error al guardar: {e}")
