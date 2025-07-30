import sys
from PyQt6.QtWidgets import QApplication
from country_picker.gui import MainWindow

def main():
    # Start app
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
