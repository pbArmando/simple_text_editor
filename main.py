import sys
from PySide6.QtWidgets import QApplication
from mi_ventana import MiVentana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiVentana()
    window.show()
    sys.exit(app.exec())