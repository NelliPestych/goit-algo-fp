import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
def __init__(self, key, color="skyblue"):
self.left = None
self.right = None
self.val = key
self.color = color
self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
if node is not None:
graph.add_node(node.id, color=node.color, label=node.val)
if node.left:
graph.add_edge(node.id, node.left.id)
l = x - 1 / 2 ** layer
pos[node.left.id] = (l, y - 1)
l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
if node.right:
graph.add_edge(node.id, node.right.id)
r = x + 1 / 2 ** layer
pos[node.right.id] = (r, y - 1)
r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
return graph

def draw_tree(tree_root, colors, labels):
tree = nx.DiGraph()
pos = {tree_root.id: (0, 0)}
tree = add_edges(tree, tree_root, pos)

node_colors = [node[1]['color'] for node in tree.nodes(data=True)]
node_labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

plt.figure(figsize=(8, 5))
nx.draw(tree, pos=pos, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors)
plt.show()

def bfs(tree):
queue = []
result = []
if tree:
queue.append(tree)
while queue:
node = queue.pop(0)
result.append(node)
if node.left:
queue.append(node.left)
if node.right:
queue.append(node.right)
return result

def dfs(tree):
stack = []
result = []
if tree:
stack.append(tree)
while stack:
node = stack.pop()
result.append(node)
if node.right:
stack.append(node.right)
if node.left:
stack.append(node.left)
return result

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з обходом в ширину (BFS)
bfs_order = bfs(root)
colors = ['#%02X%02X%02X' % (i * 20, 100, 100) for i in range(len(bfs_order))]
labels = {node.id: str(i) for i, node in enumerate(bfs_order)}
for i, node in enumerate(bfs_order):
node.color = colors[i]
draw_tree(root, colors, labels)

# Відображення дерева з обходом в глибину (DFS)
dfs_order = dfs(root)
colors = ['#%02X%02X%02X' % (i * 20, 100, 100) for i in range(len(dfs_order))]
labels = {node.id: str(i) for i, node in enumerate(dfs_order)}
for i, node in enumerate(dfs_order):
node.color = colors[i]
draw_tree(root, colors, labels)
