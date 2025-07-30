import sys
from PyQt6.QtCore import QSize, QThread
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLabel
from country_picker.helper_functions import CountryFetcher

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

        # Load countries in separate thread
        self.thread = QThread()
        self.worker = CountryFetcher()
        self.worker.moveToThread(self.thread)

        # Handle the thread
        self.thread.started.connect(self.worker.run)

        # Start the thread
        self.thread.start()
        
        # On select country, update label text to the selected country
        self.combobox.currentTextChanged.connect(self.update_label)

    def update_label(self, text: str):
        self.label.setText(f"Selected: {text}")

    def show_error(self, message: str):
        self.label.setText(f"Error: {message}")

    def populate_combobox(self, countries: list[str]):
        self.combobox.addItems(countries)
        self.update_label(self.combobox.currentText())
