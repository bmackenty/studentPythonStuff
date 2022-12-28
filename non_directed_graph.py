# this code WAS NOT written by me
#  it was written by chatAI

import random
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, src, dest, weight):
        self.adj_matrix[src][dest] = weight
        self.adj_matrix[dest][src] = weight

# Create the graph with 100 nodes
g = Graph(100)

# Add edges to the graph with random weights between 1 and 10
for i in range(100):
    num_edges = random.randint(1, 10) # Change this line
    for j in random.sample(range(100), num_edges):
        if i != j:
            weight = random.randint(1, 10)
            g.add_edge(i, j, weight)

# Create a NetworkX graph
nx_graph = nx.Graph()

# Add nodes to the graph
for i in range(100):
    nx_graph.add_node(i)

# Add edges to the graph
for i in range(100):
    for j in range(i+1, 100):
        if g.adj_matrix[i][j] > 0:
            nx_graph.add_edge(i, j, weight=g.adj_matrix[i][j])

# Draw the graph
pos = nx.circular_layout(nx_graph)
nx.draw(nx_graph, pos, with_labels=True, font_weight='bold')

# Show the graph
plt.show()
