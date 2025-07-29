import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLabel
from helper_functions import fetch_country_names

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
                
        # Window config
        self.setWindowTitle("Eilert Tunheim - BE-CSS-GTA-2025-83-GRAE Exercise")
        self.setFixedSize(QSize(600, 400))
        
        # Central widget and layout
        central_widget = QWidget()
        vbox = QVBoxLayout()
        
        # Combobox config
        self.combobox = QComboBox()
        
        # Label config
        self.label = QLabel("")
        
        # Add widgets
        vbox.addWidget(self.combobox)
        vbox.addWidget(self.label)
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Fetch countries and add to combobox
        countries = fetch_country_names()
        self.combobox.addItems(countries)
        
        # On select country, update label text to the selected country
        self.combobox.currentTextChanged.connect(self.update_label)

    def update_label(self, text: str):
        self.label.setText(f"Selected: {text}")


# Start app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
