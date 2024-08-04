import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

# Приклад використання
graph = Graph()
for node in range(6):
    graph.add_node(node)

graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 5, 14)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 11)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 5, 9)

visited, path = dijkstra(graph, 0)
print("Відстані до всіх вузлів:", visited)
print("Шлях:", path)
