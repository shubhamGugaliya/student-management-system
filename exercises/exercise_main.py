from PyQt6.QtGui import QDropEvent
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average speed calculator")
        grid = QGridLayout()

        # create widgets
        distance_label = QLabel("Distance ")
        self.distance_label_edit = QLineEdit()

        time_label = QLabel(" Time in Hours ")
        self.time_label_edit = QLineEdit()

        self.combobox1 = QComboBox()
        self.combobox1.addItem('imperial (miles)')
        self.combobox1.addItem('Kilometers')
        print(self.combobox1.currentText())

        calculate_button = QPushButton("calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(self.combobox1,0,2)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        if self.combobox1.currentText() == "imperial (miles)":
            average_speed = (int(self.distance_label_edit.text()) / int(self.time_label_edit.text())) *0.621371
            self.output_label.setText(f"Average speed is {average_speed} miles per hour" )

        elif self.combobox1.currentText() == "Kilometers":
            average_speed = int(self.distance_label_edit.text()) / int(self.time_label_edit.text())
            self.output_label.setText(f"Average speed is {average_speed} kmph")

            print(average_speed)






app = QApplication(sys.argv)
speedcalculator = SpeedCalculator()
speedcalculator.show()
sys.exit(app.exec())
