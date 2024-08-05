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
    # Відстані до всіх вузлів
    distances = {node: float('infinity') for node in graph.nodes}
    distances[initial] = 0

    # Батьківський вузол для побудови шляху
    previous_nodes = {node: None for node in graph.nodes}

    # Бінарна купа
    priority_queue = [(0, initial)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.edges[current_node]:
            distance = current_distance + graph.distances[(current_node, neighbor)]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

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

distances, previous_nodes = dijkstra(graph, 0)
print("Відстані до всіх вузлів:", distances)
print("Шлях:", previous_nodes)
