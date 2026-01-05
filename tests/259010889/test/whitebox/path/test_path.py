import unittest
from core.route_engine import RouteEngine
from core.file_handler import FileHandler

class TestPathCoverage(unittest.TestCase):

    def setUp(self):
        FileHandler.save_map({
            "locations":{"A":{}, "B":{}, "C":{}},
            "paths":{"A":["B"],"B":["A","C"],"C":["B"]}
        })

    def test_path_exists(self):
        self.assertEqual(RouteEngine.shortest_path("A","C"),["A","B","C"])

    def test_path_not_exists(self):
        self.assertIsNone(RouteEngine.shortest_path("A","D"))

if __name__ == "__main__":
    unittest.main()
