import unittest
from core.map_manager import MapManager
from core.file_handler import FileHandler

class TestStatementCoverage(unittest.TestCase):

    def setUp(self):
        FileHandler.save_map({"locations":{}, "paths":{}})

    def test_all_statements(self):
        MapManager.add_location("A","Academic",(1,1))
        MapManager.update_location("A","Library",(2,2))
        MapManager.search_by_name("A")
        MapManager.search_by_category("Library")
        MapManager.remove_location("A")

if __name__ == "__main__":
    unittest.main()
