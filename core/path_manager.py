from core.file_handler import FileHandler

class PathManager:

    @staticmethod
    def detect_unreachable_locations():
        data = FileHandler.load_map()
        locations = set(data["locations"].keys())
        paths = data["paths"]

        if not locations:
            return []

        visited = set()
        start = next(iter(locations))

        def dfs(node):
            visited.add(node)
            for neigh in paths.get(node, []):
                if neigh not in visited:
                    dfs(neigh)

        dfs(start)
        return list(locations - visited)

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

    @staticmethod
    def step_by_step_directions(path):
        if not path or len(path) < 2:
            return []

        steps = []
        for i in range(len(path) - 1):
            steps.append(f"Step {i+1}: Go from {path[i]} to {path[i+1]}")
        return steps
