import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

import unittest
from core.validator import Validator

class TestValidatorEquivalence(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(Validator.validate_location_name("Library")[0])

    def test_empty_name(self):
        self.assertFalse(Validator.validate_location_name("")[0])

    def test_invalid_chars(self):
        self.assertFalse(Validator.validate_location_name("Lab@1")[0])

    def test_non_string(self):
        self.assertFalse(Validator.validate_location_name(123)[0])

    def test_valid_speed(self):
        self.assertTrue(Validator.validate_speed("5")[0])

    def test_zero_speed(self):
        self.assertFalse(Validator.validate_speed("0")[0])

    def test_invalid_speed(self):
        self.assertFalse(Validator.validate_speed("abc")[0])

if __name__ == "__main__":
    unittest.main()
