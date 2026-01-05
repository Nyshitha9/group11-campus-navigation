import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

import unittest
from core.validator import Validator


class TestCoordinatesBVA(unittest.TestCase):

    def test_lower_boundary(self):
        self.assertTrue(Validator.validate_coordinates((0,0))[0])

    def test_upper_boundary(self):
        self.assertTrue(Validator.validate_coordinates((5000,5000))[0])

    def test_below_boundary(self):
        self.assertFalse(Validator.validate_coordinates((-1,10))[0])

    def test_above_boundary(self):
        self.assertFalse(Validator.validate_coordinates((10,6000))[0])

    def test_invalid_tuple(self):
        self.assertFalse(Validator.validate_coordinates((10,))[0])

if __name__ == "__main__":
    unittest.main()
