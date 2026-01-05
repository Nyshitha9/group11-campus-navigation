import math
from core.file_handler import FileHandler

# Terminal color codes
class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    END = "\033[0m"

def success(msg):
    return f"{Color.GREEN}{msg}{Color.END}"

def error(msg):
    return f"{Color.RED}{msg}{Color.END}"

def info(msg):
    return f"{Color.CYAN}{msg}{Color.END}"

def warn(msg):
    return f"{Color.YELLOW}{msg}{Color.END}"


# Find nearest neighbor to a newly added location
def nearest_locations(name, limit=3):
    data = FileHandler.load_map()
    locs = data["locations"]

    if name not in locs:
        return []

    x1, y1 = locs[name]["coords"]

    distances = []
    for other, info in locs.items():
        if other == name:
            continue
        x2, y2 = info["coords"]
        d = math.dist((x1, y1), (x2, y2))
        distances.append((other, d))

    distances.sort(key=lambda x: x[1])
    return [loc for loc, dist in distances[:limit]]


# ASCII Map Display
def ascii_map():
    data = FileHandler.load_map()
    paths = data["paths"]

    print("\n--- ASCII MAP ---")
    for loc in paths:
        connections = " --- ".join(paths[loc])
        print(f"{loc} --> {connections}")
