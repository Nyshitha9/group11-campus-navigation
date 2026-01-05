import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../..")))

import unittest
from core.map_manager import MapManager
from core.file_handler import FileHandler

class TestMapManagerCategory(unittest.TestCase):

    def setUp(self):
        FileHandler.save_map({"locations":{}, "paths":{}})

    def test_add_valid_location(self):
        ok,_ = MapManager.add_location("Lab","Academic",(10,10))
        self.assertTrue(ok)

    def test_add_duplicate(self):
        MapManager.add_location("Lab","Academic",(10,10))
        ok,_ = MapManager.add_location("Lab","Academic",(10,10))
        self.assertFalse(ok)

    def test_remove_existing(self):
        MapManager.add_location("Hostel","Hostel",(20,20))
        ok,_ = MapManager.remove_location("Hostel")
        self.assertTrue(ok)

    def test_remove_missing(self):
        ok,_ = MapManager.remove_location("Unknown")
        self.assertFalse(ok)

if __name__ == "__main__":
    unittest.main()
