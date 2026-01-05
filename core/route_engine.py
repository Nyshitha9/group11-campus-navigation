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
