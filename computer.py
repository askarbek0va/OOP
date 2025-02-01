class Computer:
    # constructor
     def __init__(self, brand, model, processor=None, RAM= None):
         self.brand=brand
         self.model=model
         self.processor=processor
         self.RAM=RAM

     def __str__(self):
        return f'{self.brand} {self.model} {self.processor} {self.RAM}'

     # methods
     def display_info(self):
         print(f'Computer brand:{self.brand} , Model:{self.model}, Processor:{self.processor}, RAM:{self.RAM}')

     def awesome(self):
         print(f'Your computer {self.brand} {self.model} is awesome!')




