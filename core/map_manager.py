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
