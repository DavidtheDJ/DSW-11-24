#David Justice
#11-30-16
#Basic PyQt App

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    """this class creates a main windows to observe the growth of a simpulation"""

    #constructor
    def __init__(self):
        super().__init__()  #call super class constuctor
        self.setWindowTitle("Crop Simulator") #set window title


def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instace of main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raise instance to top of window stack
    crop_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
