import unittest
from models import Supervisor


class SupervisorTestCase(unittest.TestCase):
    def setUp(self):
        self.supervisor = Supervisor.login("yasin", "1234")
        self.sample = Supervisor.sample()

    def test_all_data(self):
        self.assertIsInstance(
            self.sample, Supervisor, "sample does not return proper instance"
        )
        self.assertTrue(hasattr(self.sample, "username"), "instance")
        self.assertTrue(hasattr(self.sample, "password"))
        self.assertTrue(hasattr(self.sample, "phone_number"))
        self.assertFalse(self.sample.logged_in, "Login is not False by default")

    def test_supervisor_protected_method(self):
        self.assertIsNone(self.sample.protected(), "Not raised on protected method")
        self.assertListEqual(
            self.supervisor.protected(), [1, 2, 3], "Protected data dont match"
        )
