import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow,QLineEdit, QPushButton
from model import CalculatorModel


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), 'calculator.ui')
        uic.loadUi(ui_path, self)

        self.calculator=CalculatorModel()

        self.button0.clicked.connect(lambda: self.on_click_digit('0'))
        self.button1.clicked.connect(lambda: self.on_click_digit('1'))
        self.button2.clicked.connect(lambda: self.on_click_digit('2'))
        self.button3.clicked.connect(lambda: self.on_click_digit('3'))
        self.button4.clicked.connect(lambda: self.on_click_digit('4'))
        self.button5.clicked.connect(lambda: self.on_click_digit('5'))
        self.button6.clicked.connect(lambda: self.on_click_digit('6'))
        self.button7.clicked.connect(lambda: self.on_click_digit('7'))
        self.button8.clicked.connect(lambda: self.on_click_digit('8'))
        self.button9.clicked.connect(lambda: self.on_click_digit('9'))


        self.buttonp.clicked.connect(lambda: self.on_click_digit('+'))
        self.buttonm.clicked.connect(lambda: self.on_click_digit('-'))
        self.buttonx.clicked.connect(lambda: self.on_click_digit('*'))
        self.buttond.clicked.connect(lambda: self.on_click_digit('/'))
        self.buttont.clicked.connect(lambda: self.on_click_digit('.'))

        self.buttonc.clicked.connect(self.on_click_clear)
        self.buttone.clicked.connect(self.on_click_result)
        self.buttonr.clicked.connect(self.remove_last_character)
        self.buttonper.clicked.connect(lambda: self.on_click_digit('%'))


    def on_click_digit(self,digit):
        self.calculator.add_to_expression(digit)
        self.input.setText(self.calculator.get_expression())

    def on_click_result(self):
        result=self.calculator.calculate()
        self.calculator.expression = result
        self.input.setText(self.calculator.get_expression())

    def on_click_clear(self):
        self.calculator.clear_expression()
        self.input.setText(self.calculator.get_expression())

    def remove_last_character(self):
        self.calculator.remove_last_character()
        self.input.setText(self.calculator.get_expression())

    def on_click_percent(self):
        self.calculator.add_to_expression('%')



