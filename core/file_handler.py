import json
import os
from datetime import datetime

class FileHandler:

    FILE_PATH = "data/map.json"
    VERSION_DIR = "data/versions"

    @staticmethod
    def load_map():
        if not os.path.exists(FileHandler.FILE_PATH):
            return {"locations": {}, "paths": {}}

        try:
            with open(FileHandler.FILE_PATH, "r") as f:
                return json.load(f)
        except:
            return {"locations": {}, "paths": {}}
        
    @staticmethod
    def save_map(data):
        with open(FileHandler.FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)
        return True

    @staticmethod
    def backup_map(data):
        os.makedirs(FileHandler.VERSION_DIR, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_{ts}.json"
        backup_path = os.path.join(FileHandler.VERSION_DIR, backup_file)

        with open(backup_path, "w") as f:
            json.dump(data, f, indent=4)

        return backup_path
