import sqlite3
from entities import Employee

class EmployeeDAO():

    def __init__(self,databasefile):
        self.conn=sqlite3.connect(databasefile)
        self.cursor=self.conn.cursor()


    def get_by_id(self,id):
        sql ='''
            SELECT *
            FROM employee
            WHERE id = ?
        '''

        self.cursor.execute(sql, _parameters:(id,))
        row=self.cursor.fetchone()

        if row:
            employee=Employee(id=row[0],name=row[1],position=row[2],salary=row[3],hire_date=row[4])
        else:
            employee=None

        return employee