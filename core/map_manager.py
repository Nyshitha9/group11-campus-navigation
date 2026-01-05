from core.file_handler import FileHandler
from core.validator import Validator
from core.utils import nearest_locations, warn, success, error


class MapManager:

    @staticmethod
    def add_location(name, category, coords):
        # Validate name
        valid, msg = Validator.validate_location_name(name)
        if not valid:
            return False, error(msg)

        # Validate coords
        valid, msg = Validator.validate_coordinates(coords)
        if not valid:
            return False, error(msg)

        data = FileHandler.load_map()

        # Prevent duplicates
        if name in data["locations"]:
            return False, error("Location already exists")

        # Add location
        data["locations"][name] = {
            "category": category,
            "coords": coords
        }

        # Create empty path list
        data["paths"].setdefault(name, [])

        FileHandler.save_map(data)

        # Suggest connections to avoid disconnects
        suggestions = nearest_locations(name)

        if suggestions:
            suggestion_msg = warn(
                f"'{name}' is currently isolated.\n"
                f"Suggested locations to connect: {suggestions}"
            )
        else:
            suggestion_msg = warn(
                f"'{name}' added but no nearby nodes found to connect."
            )

        return True, success("Location added") + "\n" + suggestion_msg

    @staticmethod
    def remove_location(name):
        data = FileHandler.load_map()

        if name not in data["locations"]:
            return False, error("Location not found")

        # Remove the location entry
        del data["locations"][name]

        # Remove location from paths
        if name in data["paths"]:
            del data["paths"][name]

        for loc in data["paths"]:
            if name in data["paths"][loc]:
                data["paths"][loc].remove(name)

        FileHandler.save_map(data)
        return True, success("Location removed")

    @staticmethod
    def update_location(name, category=None, coords=None):
        data = FileHandler.load_map()

        if name not in data["locations"]:
            return False, error("Location not found")

        # Update category if provided
        if category:
            data["locations"][name]["category"] = category

        # Update coordinates if given
        if coords:
            ok, msg = Validator.validate_coordinates(coords)
            if not ok:
                return False, error(msg)
            data["locations"][name]["coords"] = coords

        FileHandler.save_map(data)
        return True, success("Location updated")

    @staticmethod
    def search_by_name(query):
        data = FileHandler.load_map()
        return [
            loc for loc in data["locations"]
            if query.lower() in loc.lower()
        ]

    @staticmethod
    def search_by_category(category):
        data = FileHandler.load_map()
        return [
            loc for loc, info in data["locations"].items()
            if info["category"] == category
        ]

    @staticmethod
    def list_all_locations():
        data = FileHandler.load_map()
        return list(data["locations"].keys())
