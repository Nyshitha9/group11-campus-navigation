import json
import os
from datetime import datetime

class FileHandler:

    # Compute project root directory (one level above "core")
    ROOT = os.path.dirname(os.path.dirname(__file__))

    FILE_PATH = os.path.join(ROOT, "data", "map.json")
    VERSION_DIR = os.path.join(ROOT, "data", "versions")

    @staticmethod
    def load_map():
        # Ensure directory exists
        os.makedirs(os.path.join(FileHandler.ROOT, "data"), exist_ok=True)

        # If file missing, create empty structure
        if not os.path.exists(FileHandler.FILE_PATH):
            return {"locations": {}, "paths": {}}

        try:
            with open(FileHandler.FILE_PATH, "r") as f:
                return json.load(f)
        except:
            return {"locations": {}, "paths": {}}

    @staticmethod
    def save_map(data):
        # Ensure data folder exists
        os.makedirs(os.path.join(FileHandler.ROOT, "data"), exist_ok=True)

        with open(FileHandler.FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)

        return True

    @staticmethod
    def backup_map(data):
        os.makedirs(FileHandler.VERSION_DIR, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"backup_{ts}.json"
        full_path = os.path.join(FileHandler.VERSION_DIR, filename)

        with open(full_path, "w") as f:
            json.dump(data, f, indent=4)

        return full_path
