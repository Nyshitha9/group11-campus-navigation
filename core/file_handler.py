import json
import os

class FileHandler:

    FILE_PATH = "data/map.json"

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

