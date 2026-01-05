import heapq
from core.file_handler import FileHandler

from core.file_handler import FileHandler
from core.route_engine import RouteEngine

class RouteEngine(RouteEngine):

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
