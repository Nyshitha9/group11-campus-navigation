import math
from core.file_handler import FileHandler

def find_nearest_facilities(source, category, limit=3):
    data = FileHandler.load_map()
    locations = data["locations"]

    if source not in locations:
        return []

    if category is None:
        return []

    sx, sy = locations[source]["coords"]
    results = []

    for name, info in locations.items():
        if name == source:
            continue
        if info["category"] != category:
            continue
        x, y = info["coords"]
        dist = math.dist((sx, sy), (x, y))
        results.append((name, dist))

    results.sort(key=lambda x: x[1])
    return [name for name, _ in results[:limit]]
