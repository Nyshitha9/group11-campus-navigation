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
