from core.file_handler import FileHandler
from core.validator import Validator

class MapManager:

    @staticmethod
    def add_location(name, category, coords):
        valid, msg = Validator.validate_location_name(name)
        if not valid:
            return False, msg

        valid, msg = Validator.validate_coordinates(coords)
        if not valid:
            return False, msg

        data = FileHandler.load_map()

        if name in data["locations"]:
            return False, "Location already exists."

        data["locations"][name] = {
            "category": category,
            "coords": coords
        }

        FileHandler.save_map(data)
        return True, "Location added successfully."
    
    @staticmethod
    def search_by_name(query):
        data = FileHandler.load_map()
        query = query.lower()
        return [loc for loc in data["locations"] if query in loc.lower()]
    
    @staticmethod
    def remove_location(name):
        data = FileHandler.load_map()

        if name not in data["locations"]:
            return False, "Location not found"

        del data["locations"][name]

        if name in data["paths"]:
            del data["paths"][name]

        for loc in data["paths"]:
            if name in data["paths"][loc]:
                data["paths"][loc].remove(name)

        FileHandler.save_map(data)
        return True, "Location removed."
    
    @staticmethod
    def search_by_category(category):
        data = FileHandler.load_map()
        return [n for n, info in data["locations"].items() if info["category"] == category]
    
    @staticmethod
    def update_location(name, category=None, coords=None):
        data = FileHandler.load_map()

        if name not in data["locations"]:
            return False, "Location not found"

        if category:
            data["locations"][name]["category"] = category

        if coords:
            ok, msg = Validator.validate_coordinates(coords)
            if not ok:
                return False, msg
            data["locations"][name]["coords"] = coords

        FileHandler.save_map(data)
        return True, "Updated"
    
    @staticmethod
    def list_all_locations():
        data = FileHandler.load_map()
        return list(data["locations"].keys())

    @staticmethod
    def view_location_details(name):
        data = FileHandler.load_map()
        if name not in data["locations"]:
            return False, "Location not found"
        return True, data["locations"][name]

    @staticmethod
    def filter_accessible_locations(reference, max_distance):
        data = FileHandler.load_map()
        if reference not in data["locations"]:
            return []

        rx, ry = data["locations"][reference]["coords"]
        accessible = []

        for name, info in data["locations"].items():
            x, y = info["coords"]
            distance = ((rx - x) ** 2 + (ry - y) ** 2) ** 0.5
            if distance <= max_distance:
                accessible.append(name)

        return accessible
