from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
        QLineEdit, QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        #create widgets
        name_label = QLabel("Name ")
        self.name_line_edit = QLineEdit()

        DOB_label = QLabel(" Date_of_birth MM/DD/YYYY ")
        self.DOB_line_edit = QLineEdit()

        calculate_button = QPushButton("calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel()

        
        #Add widgets to grid
        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(DOB_label,1,0)
        grid.addWidget(self.DOB_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.DOB_line_edit.text()
        birth_year = datetime.strptime(date_of_birth,"%m/%d/%Y").date().year
        age = current_year - birth_year
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old")



app = QApplication(sys.argv)
agecalculator = AgeCalculator()
agecalculator.show()
sys.exit(app.exec())
