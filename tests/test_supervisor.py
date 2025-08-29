import unittest
from models import Supervisor


class SupervisorTestCase(unittest.TestCase):
    def setUp(self):
        self.supervisor = Supervisor.login("yasin", "1234")

    def test_all_data(self):
        instance = Supervisor.sample()
        self.assertIsInstance(
            instance, Supervisor, "sample does not return proper instance"
        )
        self.assertTrue(hasattr(instance, "username"), "instance")
        self.assertTrue(hasattr(instance, "password"))
        self.assertTrue(hasattr(instance, "phone_number"))

    def test_supervisor_protected_method(self):
        self.assertIsNone(Supervisor.sample(), "Not raised on protected method")
        self.assertListEqual(
            self.supervisor.protected(), [1, 2, 3], "Protected data dont match"
        )
