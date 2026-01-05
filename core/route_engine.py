import heapq
from core.file_handler import FileHandler

class RouteEngine:

    @staticmethod
    def shortest_path(start, end):
        data = FileHandler.load_map()
        graph = data["paths"]

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

        if end not in parent:
            return None

        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    @staticmethod
    def fastest_route(start, end, speed):
        path = RouteEngine.shortest_path(start, end)
        if not path:
            return None, None
        distance = len(path) - 1
        time = distance / speed
        return path, round(time, 2)

    @staticmethod
    def alternative_routes(start, end):
        base = RouteEngine.shortest_path(start, end)
        if not base:
            return []

        data = FileHandler.load_map()
        graph = data["paths"]

        alternatives = []

        for i in range(1, len(base)-1):
            blocked = base[i]

            new_graph = {
                k: [n for n in v if n != blocked]
                for k, v in graph.items()
                if k != blocked
            }

            p = RouteEngine.shortest_path(start, end)
            if p and p != base:
                alternatives.append(p)

        return alternatives[:2]
