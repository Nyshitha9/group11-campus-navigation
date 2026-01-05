import unittest
from core.validator import Validator

class TestBranchCoverage(unittest.TestCase):

    def test_all_branches_speed(self):
        Validator.validate_speed("5")
        Validator.validate_speed("0")
        Validator.validate_speed("abc")

if __name__ == "__main__":
    unittest.main()
