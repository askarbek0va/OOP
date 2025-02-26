# Electronic Device Shopping Cart

## Overview
This project is a Python-based device management system that allows users to browse different electronic devices (Smartphones, Laptops, and Tablets), add them to a shopping cart, and perform checkout operations. The system includes classes to represent devices and their subclasses, as well as a cart for managing purchases.

## Features
- **Device Class**: Represents generic electronic devices.
- **Subclasses**: Smartphone, Laptop, and Tablet extend the Device class.
- **Shopping Cart**: Allows adding and removing devices, calculating total price, and checking out.
- **Interactive Menu**: Users can view devices, add items to the cart, and see the total price.
- **Unit Tests**: Ensures the functionality of different classes.


## Classes and Methods
### Device Class

- `display_info()`: Displays device details.
- `apply_discount(discount_percentage)`: Applies a discount to the device price.
- `is_available(amount)`: Checks if the requested quantity is available.
- `reduce_stock(amount)`: Reduces stock after purchase.

### Smartphone, Laptop, and Tablet Classes
Each subclass extends `Device` and includes additional attributes:
- **Smartphone**: `screen_size`, `battery_life`
- **Laptop**: `ram_size`, `processor_speed`
- **Tablet**: `screen_resolution`, `weight`

### Cart Class
- `add_device(device, amount)`: Adds a device to the cart.
- `get_total_price()`: Returns the total price of items in the cart.
- `print_items()`: Displays items in the cart.
- `checkout()`: Processes the purchase and updates stock.

![Снимок экрана 2025-02-26 в 14.57.10.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-26%20%D0%B2%2014.57.10.png)
![Снимок экрана 2025-02-26 в 23.50.47.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-26%20%D0%B2%2023.50.47.png)
