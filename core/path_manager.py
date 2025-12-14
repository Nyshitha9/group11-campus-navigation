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
def route_summary(path):
    if not path:
        return "No route available."

    summary = f"Route: {' -> '.join(path)}\n"
    summary += f"Stops: {len(path)-1}"
    return summary

