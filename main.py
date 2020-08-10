import sys
from PyQt5.QtWidgets import QApplication

from ventana_main import VentanaMain

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = VentanaMain()
    sys.exit(app.exec())