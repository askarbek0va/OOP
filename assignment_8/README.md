# Employee Database Management System

## Overview
This project is a Python-based Employee Database Management System that allows users to perform CRUD (Create, Read, Update, Delete) operations on an SQLite database. The system consists of an Employee entity class, an EmployeeDAO class for database operations, and a main script for testing the functionalities.

## Features
- **Create** new employees
- **Retrieve** employees by ID
- **Retrieve** all employees
- **Update** employee details
- **Delete** employees
- Prevent duplicate employee insertions


## Project Structure
```
/employee_db_project
│── employee.py       # Employee entity class
│── dao.py            # EmployeeDAO class for database operations
│── main.py           # Main script for testing CRUD operations
│── employee_db       # SQLite database file
│── README.md         # Project documentation
```

![Снимок экрана 2025-04-03 в 12.57.31.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-03%20%D0%B2%2012.57.31.png)
Employee with id=4 is deleted
Employee with id=11 and 12 are added
get_by_id() is used for id=7
