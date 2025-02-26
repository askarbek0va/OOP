from device import Device

class Smartphone(Device):

    def __init__(self,name,price,stock,warranty_period,screen_size,battery_life):
        super().__init__(name,price,stock,warranty_period)
        self.screen_size=screen_size
        self.battery_life=battery_life

    def display_info(self):
        return f"{super().display_info()}, Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours"


    def __str__(self):
        return f'Smartphone:{self.name}, Price:{self.price}, Screen size:{self.screen_size} inches, Battery life: {self.battery_life} hours'



    def make_call(self):
        return 'Smartphone can make a call'


    def install_app(self):
        return 'Install application'



class Laptop(Device):

    def __init__(self,name,price,stock,warranty_period,ram_size,processor_speed):
        super().__init__(name,price,stock,warranty_period)
        self.ram_size=ram_size
        self.processor_speed=processor_speed

    def display_info(self):
        return f"{super().display_info()}, RAM: {self.ram_size}GB, Processor Speed: {self.processor_speed} GHz"


    def __str__(self):
        return f'Laptop:{self.name}, Price:{self.price}, Ram size:{self.ram_size} GB, Processor speed: {self.processor_speed} Ghz'


    def run_program(self):
        return f'Run a program on the laptop'

    def use_keyboard(self):
        return 'You can type on the keyboard'



class Tablet(Device):
    def __init__(self,name,price,stock,warranty_period,screen_resolution,weight):
        super().__init__(name,price,stock,warranty_period)
        self.screen_resolution=screen_resolution
        self.weight=weight

    def display_info(self):
        return f"{super().display_info()}, Screen Resolution: {self.screen_resolution}, Weight: {self.weight}g"


    def __str__(self):
        return f'Tablet:{self.name}, Price:{self.price}, Screen resolution:{self.screen_resolution}, Weight: {self.weight}g'


    def browse_internet(self):
        return 'Browse the internet'


    def use_touchscreen(self):
        return "Use the touchscreen for navigation"





