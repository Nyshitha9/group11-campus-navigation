import json

class PreferenceManager:

    FILE = "data/preferences.json"

    @staticmethod
    def load():
        try:
            with open(PreferenceManager.FILE, "r") as f:
                return json.load(f)
        except:
            return {"speed": 1.0, "mode": "shortest", "quick_access": []}

    @staticmethod
    def save(speed, mode):
        data = PreferenceManager.load()
        if mode not in ["shortest", "fastest"]:
            mode = "shortest"
        data["speed"] = speed
        data["mode"] = mode
        with open(PreferenceManager.FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def add_quick_access(location):
        data = PreferenceManager.load()
        if location not in data.get("quick_access", []):
            data.setdefault("quick_access", []).append(location)
        with open(PreferenceManager.FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def get_quick_access():
        data = PreferenceManager.load()
        return data.get("quick_access", [])
