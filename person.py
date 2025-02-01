class Person:
    # constructor- special method to initialize attributes
    def __init__(self, name, surname=None, age=None, gender= None):
        self.name=name
        self.surname=surname
        self.age=age
        self.gender= gender
    # methods
    def __str__(self):
        return f' {self.name} {self.age}'
    def walk(self):
        print('Person', self.name, 'is walking')
    def info(self):
        print(f'Person {self.name} {self.surname} is {self.age} years old.')
        print('Person name =', self.name,'\n' ' surname =', self.surname,'\n' ' age =', self.age,'\n' ' gender =', self.gender )

