import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
                
        # Window config
        self.setWindowTitle("Eilert Tunheim - BE-CSS-GTA-2025-83-GRAE Exercise")
        self.setFixedSize(QSize(600, 400))
        
        # VBoxLayout config
        central_widget = QWidget()
        vbox = QVBoxLayout()
        
        # Combobox config
        self.combobox = QComboBox()
        
        # Label config
        self.label = QLabel("")
        
        # Add widget
        vbox.addWidget(self.combobox)
        vbox.addWidget(self.label)
        
        # Central widget
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)


# Start app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
