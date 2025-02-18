import unittest
from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(user_id=123456789, name="Meerim", surname="Askarbekova",
                         email="meerim.askarbekova@example.com", password="StrongPass1!",
                         birthday=datetime(2005, 12, 8))

    def test_get_details(self):
        details = self.user.get_details()
        self.assertIn('Meerim', details)
        self.assertIn("Askarbekova", details)
        self.assertIn("meerim.askarbekova@example.com", details)

    def test_get_age(self):
        expected_age = datetime.today().year - 2005
        if (datetime.today().month, datetime.today().day) < (12, 8):
            expected_age -= 1
        self.assertEqual(self.user.get_age(), expected_age)


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(user_id=123456789, name="Aiturgan", surname="Kanybekova",
                         email="aiturgan.kanybekova@example.com", password="SecurePass2@",
                         birthday=datetime(2005, 9, 2))
        UserService.users.clear()

    def test_add_and_find_user(self):
        UserService.add_user(self.user)
        found_user = UserService.find_user(123456789)
        self.assertEqual(found_user.name, "Aiturgan")

    def test_delete_user(self):
        UserService.add_user(self.user)
        UserService.delete_user(123456789)
        self.assertIsNone(UserService.find_user(123456789))

    def test_get_number(self):
        UserService.add_user(self.user)
        self.assertEqual(UserService.get_number(), 1)


class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertIsInstance(user_id, int)
        self.assertEqual(len(str(user_id)), 9)

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_generate_email(self):
        email = UserUtil.generate_email(name="Aiza", surname="Sarlykova", domain="test.com")
        self.assertEqual(email, "aiza.sarlykova@test.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("valid.email@example.com"))
        self.assertFalse(UserUtil.validate_email("invalid-email"))


if __name__ == "__main__":
    unittest.main()
