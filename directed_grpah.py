# This code was NOT WRITTEN BY ME. It was written by ChatAI. 
# this code creates a weighted directed graph with 10 nodes and random weights between 1 and 10
import random
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, src, dest, weight):
        self.adj_matrix[src][dest] = weight

# Get the number of nodes from the user
num_nodes = int(input("Enter the number of nodes: "))

# Create the graph with the specified number of nodes
g = Graph(num_nodes)

# Add edges to the graph with random weights between 1 and 10
for i in range(num_nodes):
    num_edges = random.randint(1, 10)
    for j in random.sample(range(num_nodes), num_edges):
        if i != j:
            weight = random.randint(1, 10)
            g.add_edge(i, j, weight)

# Print the adjacency matrix
print("Adjacency matrix:")
for i in range(num_nodes):
    for j in range(num_nodes):
        print(f"{g.adj_matrix[i][j]:>3}", end=" ")
    print()

# Create a NetworkX graph
nx_graph = nx.DiGraph()

# Add nodes to the graph
for i in range(num_nodes):
    nx_graph.add_node(i)

# Add edges to the graph
for i in range(num_nodes):
    for j in range(num_nodes):
        if g.adj_matrix[i][j] > 0:
            nx_graph.add_edge(i, j, weight=g.adj_matrix[i][j])

# Draw the graph
pos = nx.circular_layout(nx_graph)
nx.draw(nx_graph, pos, with_labels=True, font_weight='bold')

# Draw edge labels
edge_labels = nx.get_edge_attributes(nx_graph, 'weight')
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels)

# Show the graph
plt.show()
