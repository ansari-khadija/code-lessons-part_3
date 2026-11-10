import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges
G.add_edges_from([
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
    (4, 5)
])

# Display nodes
print("Nodes:", G.nodes())

# Display edges
print("Edges:", G.edges())

# Number of nodes
print("Number of Nodes:", G.number_of_nodes())

# Number of edges
print("Number of Edges:", G.number_of_edges())

# Find neighbors
print("Neighbors of 1:", list(G.neighbors(1)))

# Degree of each node
print("Degree:", dict(G.degree()))

# Shortest path
print("Shortest Path:", nx.shortest_path(G, 1, 5))

# Draw graph
nx.draw(
    G,
    with_labels=True,
    node_color="skyblue",
    node_size=1500,
    font_size=12
)

plt.show()