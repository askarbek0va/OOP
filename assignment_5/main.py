from device import Device
from subclasses import Smartphone
from subclasses import Laptop
from subclasses import Tablet
from cart import Cart


if __name__=='__main__':
    devices = [
        Smartphone("iPhone 13", 999, 10, 24, 6.1, 20),
        Smartphone("Samsung Galaxy S21", 799, 15, 24, 6.2, 22),
        Smartphone("Google Pixel 6", 599, 12, 24, 6.4, 18),
        Smartphone("OnePlus 9", 729, 8, 24, 6.55, 23),
        Smartphone("Xiaomi Mi 11", 699, 10, 24, 6.81, 25),
        Smartphone("Sony Xperia 5", 899, 7, 24, 6.1, 21),
        Laptop("MacBook Pro", 1999, 5, 36, 16, 3.2),
        Laptop("Dell XPS 13", 1399, 7, 24, 16, 3.1),
        Laptop("HP Spectre x360", 1299, 9, 24, 16, 3.0),
        Laptop("Asus ZenBook 14", 1099, 6, 24, 16, 2.9),
        Laptop("Lenovo ThinkPad X1", 1499, 8, 36, 16, 3.5),
        Laptop("Acer Swift 5", 999, 12, 24, 8, 2.8),
        Tablet("iPad Air", 599, 8, 18, "2360x1640", 460),
        Tablet("Samsung Galaxy Tab S7", 649, 10, 18, "2560x1600", 500),
        Tablet("Microsoft Surface Pro 7", 749, 5, 24, "2736x1824", 770),
        Tablet("Amazon Fire HD 10", 149, 20, 12, "1920x1200", 504),
        Tablet("Huawei MatePad Pro", 549, 6, 18, "2560x1600", 480),
        Tablet("Lenovo Tab P11", 399, 9, 18, "2000x1200", 450),
        Tablet("Samsung Galaxy Tab A7", 229, 15, 18, "2000x1200", 477),
        Tablet("Apple iPad Mini", 499, 10, 24, "2266x1488", 297)
    ]

    cart = Cart()


    def show_menu():
        while True:
            print("\n1. Show Devices\n2. Show Cart\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                for idx, device in enumerate(devices, start=1):
                    print(f"{idx}. {device}")
                try:
                    device_choice = int(input("Enter the number of the device to add to the cart: ")) - 1
                    if 0 <= device_choice < len(devices):
                        quantity = int(input("Enter quantity: "))
                        cart.add_device(devices[device_choice], quantity)
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == "2":
                cart.print_items()
                print(f"Total Price: ${cart.get_total_price()}")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


    show_menu()

