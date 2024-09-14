import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
import qdarktheme

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    app.setApplicationName("COM_reader")
    app.setApplicationVersion("0.1.0")
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
