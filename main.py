from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QTableWidgetItem, QDialog, QComboBox
import sys
from datetime import datetime
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student management app")

        file_menu_item = self.menuBar().addMenu("&file")
        help_menu_item = self.menuBar().addMenu("&help")

        add_student_action = QAction("add student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID","Name","Course","Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
       # print(list(result))
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert students data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        #set layout
        layout = QVBoxLayout()

        #Add student widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        #add course_name Widget
        self.course_name = QComboBox()
        self.courses = ["Math","biology","Astronomy","Physics"]
        self.course_name.addItems(self.courses)
        layout.addWidget(self.course_name)

        #Add mobile number widget
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Number")
        layout.addWidget(self.mobile_number)

        #Add button for adding student to database
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name,course,mobile) VALUES (?,?,?)",
                       (name,course,mobile))
        connection.commit()
        cursor.close()
        connection.close()
        main.load_data()


app = QApplication(sys.argv)
main = MainWindow()

main.show()
main.load_data()
sys.exit(app.exec())