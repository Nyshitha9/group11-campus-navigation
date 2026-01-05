import unittest
from core.validator import Validator

class TestConcolic(unittest.TestCase):

    def test_concolic_speed(self):
        concrete = "3"
        self.assertTrue(Validator.validate_speed(concrete)[0])
        self.assertFalse(Validator.validate_speed("0")[0])
        self.assertFalse(Validator.validate_speed("abc")[0])

if __name__ == "__main__":
    unittest.main()
