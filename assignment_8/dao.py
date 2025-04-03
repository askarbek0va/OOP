import sqlite3
from employee import Employee

class EmployeeDAO():

    def __init__(self,db_file='employee_db'):
        self.conn=sqlite3.connect(db_file)
        self.cursor=self.conn.cursor()

    def get_all(self):
        sql= 'SELECT * FROM employee'
        self.cursor.execute(sql)

        rows=self.cursor.fetchall()
        employees=[]
        for row in rows:
             e = Employee(id=row[0], name=row[1], position=row[2], salary=row[3],hire_date=row[4])
             employees.append(e)

        return employees

    def get_by_id(self,id):
        sql ='''
            SELECT *
            FROM employee
            WHERE id = ?
        '''

        self.cursor.execute(sql, (id,))
        row=self.cursor.fetchone()

        if row:
            employee=Employee(id=row[0],name=row[1],position=row[2],salary=row[3],hire_date=row[4])
        else:
            employee=None

        return employee

    def insert(self, employee:Employee):

        self.cursor.execute("SELECT id FROM employee WHERE name = ? AND hire_date = ?",
                            (employee.name, employee.hire_date))
        existing = self.cursor.fetchone()

        if existing:
            print(f"Employee '{employee.name}' already exists. Skipping insertion.")
            return existing[0]
        sql ='''
        INSERT INTO employee(name,position,salary,hire_date)
        VALUES(?,?,?,?)
        '''
        self.cursor.execute(sql,(employee.name,employee.position,employee.get_salary(),employee.hire_date))

        self.conn.commit()

        return self.cursor.lastrowid

    def update(self, employee:Employee):

        sql = '''
                   UPDATE employee
                   SET name = ?, position = ?, salary=?, hire_date=?
                   WHERE id = ?
               '''

        self.cursor.execute(sql, (employee.name,employee.position,employee.get_salary(),employee.hire_date,employee.get_id()))
        self.conn.commit()

        return self.cursor.rowcount

    def delete(self, id):
        sql = '''
            DELETE FROM employee
            WHERE id = ?
        '''
        self.cursor.execute(sql, (id,))
        self.conn.commit()

        return self.cursor.rowcount

    def close(self):
        self.conn.close()


