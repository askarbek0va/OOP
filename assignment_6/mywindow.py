from PyQt6.QtWidgets import QMainWindow,QLineEdit, QPushButton,QLabel,QMessageBox
import os
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input1=QLineEdit(self)
        self.input2=QLineEdit(self)
        self.label_8=QLabel(self)
        self.button1=QPushButton(self)


        ui_path=os.path.join(os.path.dirname(__file__),'mywindow.ui')
        uic.loadUi(ui_path,self)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Enter your weight and height")

        self.button1.clicked.connect(self.on_click)

        self.actionExit.triggered.connect(QApplication.quit)
        self.actionClear.triggered.connect(self.clear_inputs)
        self.actionInformation.triggered.connect(self.show_information)




    def on_click(self):
        val1=self.input1.text()
        val2=self.input2.text()
        bmi=round(int(val1)/(((int(val2))/100)**2),1)
        self.button1.setText(str(bmi))

        if bmi < 18.5:
            status = "Underweight"
            color="rgb(255, 212, 121)"
            self.button1.setStyleSheet("background-color: rgb(255, 212, 121)")
        elif 18.5 <=bmi <25:
            status = "Normal weight"
            color="rgb(0, 143, 0)"
            self.button1.setStyleSheet("background-color: rgb(0, 143, 0)")
        elif 25<=bmi <30:
            status = "Overweight"
            color="rgb(255, 147, 0)"
            self.button1.setStyleSheet("background-color: rgb(255, 147, 0)")
        else:
            status = "Obese"
            color="rgb(157, 44, 26)"
            self.button1.setStyleSheet("background-color: rgb(157, 44, 26)")

        self.statusBar().showMessage(f"BMI Status: {status}")

        self.statusbar.setStyleSheet(f"background-color: {color}")

    def clear_inputs(self):
        self.input1.clear()
        self.input2.clear()
        self.button1.setText("Calculate BMI")
        self.button1.setStyleSheet("")

    def show_information(self):
        QMessageBox.information(self, "Information about BMI Calculator",
                                "This is a simple BMI calculator.\n\n"
                                "Enter your weight (kg) and height (cm) to calculate BMI.\n\n"
                                "BMI Categories:\n"
                                "- Underweight: <18.5\n"
                                "- Normal weight: 18.5 - 25\n"
                                "- Overweight: 25 - 30\n"
                                "- Obese: 30+")