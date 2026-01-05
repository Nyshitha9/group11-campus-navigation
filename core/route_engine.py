import heapq
from core.file_handler import FileHandler

class RouteEngine:

    @staticmethod
    def shortest_path(start, end):
        data = FileHandler.load_map()
        graph = data["paths"]

        if start not in graph or end not in graph:
            return None

        dist = {loc: float("inf") for loc in graph}
        dist[start] = 0
        pq = [(0, start)]
        parent = {}

        while pq:
            d, node = heapq.heappop(pq)
            if node == end:
                break

            for neigh in graph.get(node, []):
                if d + 1 < dist[neigh]:
                    dist[neigh] = d + 1
                    parent[neigh] = node
                    heapq.heappush(pq, (dist[neigh], neigh))

        if start == end:
            return [start]

        if end not in parent:
            return None

        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    @staticmethod
    def fastest_route(start, end, speed):
        if speed <= 0:
            return None, None

        path = RouteEngine.shortest_path(start, end)
        if not path:
            return None, None

        distance = len(path) - 1
        time = distance / speed
        return path, round(time, 2)

    @staticmethod
    def multi_criteria_route(start, end, speed, preference):
        if preference == "shortest":
            return RouteEngine.shortest_path(start, end)
        if preference == "fastest":
            path, _ = RouteEngine.fastest_route(start, end, speed)
            return path
        return None

    @staticmethod
    def alternative_routes(start, end):
        base_path = RouteEngine.shortest_path(start, end)
        if not base_path or len(base_path) <= 2:
            return []

        data = FileHandler.load_map()
        graph = data["paths"]
        alternatives = []

        for i in range(1, len(base_path) - 1):
            blocked = base_path[i]
            new_graph = {}

            for node, neighs in graph.items():
                if node == blocked:
                    continue
                new_graph[node] = [n for n in neighs if n != blocked]

            original_paths = data["paths"]
            data["paths"] = new_graph

            alt = RouteEngine.shortest_path(start, end)
            if alt and alt != base_path and alt not in alternatives:
                alternatives.append(alt)

            data["paths"] = original_paths

        return alternatives
