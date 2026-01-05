import unittest
import random
from core.validator import Validator

class TestRandomInputs(unittest.TestCase):

    def test_random_speeds(self):
        for _ in range(20):
            speed = random.uniform(-10,10)
            result,_ = Validator.validate_speed(str(speed))
            if speed <= 0:
                self.assertFalse(result)
            else:
                self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
