import sqlite3

class Employee:
    def __init__(self, id:int,name:str,position:str,salary,hire_date):
        self.__id=id
        self.name=name
        self.position=position
        self.__salary=salary
        self.hire_date=hire_date


    def __str__(self):
        return f'Employee id={self.__id}, name={self.name}, position={self.position}, salary={self.__salary}, hire_date={self.hire_date}'

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        self.__salary=salary





