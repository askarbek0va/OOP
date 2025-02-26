import unittest
from device import Device
from subclasses import  Smartphone, Laptop, Tablet
from cart import Cart


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device("Test Device", 100, 6, 12)

    def test_display_info(self):
        self.assertEqual(self.device.__str__(), "Device name: Test Device, Price: 100, Stock:6, Warranty:12 months")

    def test_apply_discount(self):
        self.device.apply_discount(10)
        self.assertEqual(self.device.price, 90)

    def test_is_available(self):
        self.assertTrue(self.device.is_available(2))
        self.assertFalse(self.device.is_available(10))

    def test_reduce_stock(self):
        self.device.reduce_stock(2)
        self.assertEqual(self.device.stock, 4)


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.phone = Smartphone("iPhone", 1000, 5, 24, 6.1, 20)

    def test_display_info(self):
        expected_info = "Device name: iPhone, Price: 1000, Stock:5, Warranty:24 months, Screen Size: 6.1 inches, Battery Life: 20 hours"
        self.assertEqual(self.phone.display_info(), expected_info)

    def test_make_call(self):
        self.assertEqual(self.phone.make_call(), "Smartphone can make a call")


class TestLaptop(unittest.TestCase):
    def setUp(self):
        self.laptop = Laptop("MacBook", 2000, 3, 36, 16, 3.2)

    def test_display_info(self):
        expected_info = "Device name: MacBook, Price: 2000, Stock:3, Warranty:36 months, RAM: 16GB, Processor Speed: 3.2 GHz"
        self.assertEqual(self.laptop.display_info(), expected_info)

    def test_run_program(self):
        self.assertEqual(self.laptop.run_program(), 'Run a program on the laptop')


class TestTablet(unittest.TestCase):
    def setUp(self):
        self.tablet = Tablet("iPad", 500, 8, 18, "2360x1640", 460)

    def test_display_info(self):
        expected_info = "Device name: iPad, Price: 500, Stock:8, Warranty:18 months, Screen Resolution: 2360x1640, Weight: 460g"
        self.assertEqual(self.tablet.display_info(), expected_info)

    def test_browse_internet(self):
        self.assertEqual(self.tablet.browse_internet(), "Browse the internet")


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.device1 = Device("Device1", 100, 5, 12)
        self.device2 = Device("Device2", 200, 3, 24)

    def test_add_device(self):
        self.cart.add_device(self.device1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.get_total_price(), 200)

    def test_get_total_price(self):
        self.cart.add_device(self.device1, 1)
        self.cart.add_device(self.device2, 1)
        self.assertEqual(self.cart.get_total_price(), 300)

    def test_checkout(self):
        self.cart.add_device(self.device1, 2)
        self.cart.checkout()
        self.assertEqual(self.cart.get_total_price(), 200)
        self.assertEqual(len(self.cart.items), 1)

if __name__ == "__main__":
    unittest.main()