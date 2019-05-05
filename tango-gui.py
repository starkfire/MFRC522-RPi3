import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TangoGUI():
    ' graphical user interface for Jeepney Automated Ticketing System '

    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        main = QWidget()
        layout = QGridLayout()
        # Widgets
        statusb = QPushButton('Status')
        consoleb = QPushButton('Console Output')
        # Add Widgets
        layout.addWidget(statusb,0,1)
        layout.addWidget(consoleb,0,2)
        # Call Functions
        def statusb_click():
            self.statusWindow()
            layout.addWidget(self.statusw,1,1,1,4)
        def consoleb_click():
            self.consoleWindow()
            layout.addWidget(self.consolew,1,1,1,4)
        # Setup
        main.setLayout(layout)
        main.setWindowTitle("Jeepney Automated Ticketing Session")
        # Behavior
        statusb.clicked.connect(statusb_click)
        consoleb.clicked.connect(consoleb_click)
        # Execute
        main.show()
        app.exec_()

    def statusWindow(self):
        self.statusw = QGroupBox("Status")
        wlayout = QFormLayout()
        wlayout.addRow(QLabel("Current Location: "))
        wlayout.addRow(QLabel("Total Income: "))
        self.statusw.setLayout(wlayout)

    def consoleWindow(self):
        self.consolew = QGroupBox("Console")
        clayout = QGridLayout()
        self.consolew.setLayout(clayout)

if __name__ == '__main__':
    app = QApplication([])
    tango = TangoGUI()
    tango.main()
