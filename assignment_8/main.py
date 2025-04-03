from dao import EmployeeDAO
from employee import Employee

if __name__=='__main__':
    dao=EmployeeDAO('employee_db')

    emp1 = Employee(id=11,name="Ethan White", position="Marketing Manager", salary=72000,hire_date='2023-01-25')
    row=dao.update(emp1)
    dao.insert(emp1)
    emp4 = Employee(id=12,name="Karen Adams", position="Graphic Designer", salary=80000, hire_date='2023-07-22')
    row = dao.update(emp4)
    dao.insert(emp4)


    dao.delete(4)

    employees = dao.get_all()
    for emp in employees:
        print(emp)

    em = dao.get_by_id(7)
    print(em)

    dao.close()



