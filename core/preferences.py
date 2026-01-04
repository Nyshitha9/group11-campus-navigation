import json

class PreferenceManager:

    FILE = "data/preferences.json"

    @staticmethod
    def load():
        try:
            with open(PreferenceManager.FILE, "r") as f:
                return json.load(f)
        except:
            return {"speed": 1.0, "mode": "shortest"}

    @staticmethod
    def save(speed, mode):
        if mode not in ["shortest", "fastest"]:
            mode = "shortest"
        with open(PreferenceManager.FILE, "w") as f:
            json.dump({"speed": speed, "mode": mode}, f, indent=4)
