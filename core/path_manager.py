from map_manager import FileHandler

@staticmethod
def validate_connectivity():
    data = FileHandler.load_map()
    if not data["locations"]:
        return False

    visited = set()
    start = next(iter(data["locations"]))

    def dfs(node):
        visited.add(node)
        for n in data["paths"].get(node, []):
            if n not in visited:
                dfs(n)

    dfs(start)
    return len(visited) == len(data["locations"])

@staticmethod
def add_path(a, b):
    data = FileHandler.load_map()

    if a not in data["locations"] or b not in data["locations"]:
        return False, "Locations missing"

    data["paths"].setdefault(a, []).append(b)
    data["paths"].setdefault(b, []).append(a)

    FileHandler.save_map(data)
    return True, "Path added"

