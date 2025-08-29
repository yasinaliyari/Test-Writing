import unittest
from models import Supervisor


class SupervisorTestCase(unittest.TestCase):
    def test_all_data(self):
        instance = Supervisor.sample()
        self.assertIsInstance(
            instance, Supervisor, "sample does not return proper instance"
        )
        self.assertTrue(hasattr(instance, "username"), "instance")
        self.assertTrue(hasattr(instance, "password"))
        self.assertTrue(hasattr(instance, "phone_number"))
