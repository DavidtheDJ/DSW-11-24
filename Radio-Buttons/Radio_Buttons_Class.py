#David Justice
#11-30-16
#Radio Buttons PyQt App

import sys

from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """this class creates a group pf radio buttons from a given lists of labels"""

    #constructor
    def __init__(self, label, instruction,button_list):
        super().__init__()  #call super class constuctor

        #create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()

        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set the defult checked item
        self.radio_button_list[0].setChecked(True)

        #create layout for radio buttons and add them
        self.radio_button_layout = QVBoxLayout()

        #add buttons to the layout and button group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter += 1

        #add radio buttons to the group box
        self.radio_group_box.setLayout(self.radio_button_layout)

        #create a layout for a whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        #set the layout for this widget
        self.setLayout(self.main_layout)

    #method to find out the selected button
    def selected_button(self):
        return self.radio_button_group.checkedId()
            


def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instace of main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raise instance to top of window stack
    crop_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
