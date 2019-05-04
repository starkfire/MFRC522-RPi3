import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TangoGUI():
	' graphical user interface for RFID Ticketing System '
	
	def __init__(self):
		super().__init__()
		self.title = 'RFID-Ticketing'
		self.initialize()

	def initialize(self):
		main = QWidget()
		layout = QGridLayout()


if __name__ == '__main__':
	app = QApplication([])
	tango = TangoGUI()