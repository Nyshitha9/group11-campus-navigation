from core.file_handler import FileHandler

class PathManager:

    @staticmethod
    def add_path(a, b):
        data = FileHandler.load_map()

        if a not in data["locations"] or b not in data["locations"]:
            return False, "Invalid locations"

        data["paths"].setdefault(a, []).append(b)
        data["paths"].setdefault(b, []).append(a)

        FileHandler.save_map(data)
        return True, "Path added"

    @staticmethod
    def remove_path(a, b):
        data = FileHandler.load_map()

        if a in data["paths"] and b in data["paths"][a]:
            data["paths"][a].remove(b)

        if b in data["paths"] and a in data["paths"][b]:
            data["paths"][b].remove(a)

        FileHandler.save_map(data)
        return True, "Path removed"

    @staticmethod
    def validate_connectivity():
        data = FileHandler.load_map()
        if not data["locations"]:
            return False

        visited = set()
        start = next(iter(data["locations"]))

        def dfs(node):
            visited.add(node)
            for neigh in data["paths"].get(node, []):
                if neigh not in visited:
                    dfs(neigh)

        dfs(start)
        return len(visited) == len(data["locations"])

    @staticmethod
    def route_summary(path):
        if not path:
            return "No route available."

        summary = f"Route: {' -> '.join(path)}\n"
        summary += f"Stops: {len(path)-1}"
        return summary
