import unittest
from core.validator import Validator

class TestSymbolicExecution(unittest.TestCase):

    def test_symbolic_paths_speed(self):
        self.assertFalse(Validator.validate_speed("abc")[0])
        self.assertFalse(Validator.validate_speed("0")[0])
        self.assertTrue(Validator.validate_speed("5")[0])

if __name__ == "__main__":
    unittest.main()
