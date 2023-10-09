import networkx as nx
import matplotlib.pyplot as plt

# Define the cities as nodes
# cities = ['A', 'B', 'C', 'D', 'E']

# Add nodes for 14 cities
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'M', 'N', 'P']

# Define the edges between the cities
edges = [('A', 'G', 116),('A', 'H', 142),('A', 'K', 75),('A', 'D', 295) , 
         ('B', 'E', 162),('B', 'J', 184),('B', 'M', 323),
         ('C', 'P', 127),('C', 'K', 189),('C', 'L', 92.6),
         ('D', 'E', 183),('D', 'A', 295),('D', 'M', 290),('D', 'N', 204),('D', 'E', 183),('D', 'J', 97.1),('D', 'F', 200),
         ('E', 'B', 162),('E', 'J', 119),('E', 'D', 183),('E', 'F', 66), 
         ('F', 'H', 74.2),('F', 'E', 66),('F', 'D', 200),
         ('G', 'H', 126),('G', 'A', 116),
         ('H', 'G', 126),('H', 'F', 74.2),('H', 'A', 142),
         ('J', 'B', 184),('J', 'E', 119),('J', 'D', 97.1),('J', 'M', 335),
         ('K', 'A', 75),('K', 'C', 189),('K', 'L', 96),
         ('L', 'K', 96),('L', 'C', 92.6),
         ('M', 'B', 323),('M', 'D', 290),('M', 'J', 335),('M', 'N', 246),
         ('N', 'M', 246),('N', 'D', 204),('N', 'P', 197),
         ('P', 'D', 170),('P', 'N', 197),('P', 'C', 127)]
# Create the graph object
G = nx.Graph()

# Add the nodes to the graph
G.add_nodes_from(cities)

# Add the edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Draw the graph with city labels and edge weights
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Show the graph
plt.show()