
class Device:
    def __init__(self,name,price,stock,warranty_period):
        self.name=name
        self.price=price
        self.stock=stock
        self.warranty_period=warranty_period


    def display_info(self):
        return f'Device name: {self.name}, Price: {self.price}, Stock:{self.stock}, Warranty:{self.warranty_period} months'

    def __str__(self):
        return f'Device name: {self.name}, Price: {self.price}, Stock:{self.stock}, Warranty:{self.warranty_period} months'

    def apply_discount(self,discount_percentage):
        self.price= self.price - self.price * discount_percentage/100
        return

    def is_available(self,amount):
        if self.stock>=amount:
            return True
        return False

    def reduce_stock(self,amount):
        if self.is_available(amount):
             self.stock -= amount
        else:
            print(f"Not enough stock for {self.name}.")

