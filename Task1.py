import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()

# Adjusted positions to ensure Green Park, Piccadilly Circus, and Leicester Square have the same y-coordinate
positions = {
    'Hyde Park Corner': (5.2, 1.7),
    'Green Park': (5.6, 2),
    'Piccadilly Circus': (7.2, 2),
    'Leicester Square': (8, 2),
    'Covent Garden': (9.2, 3),
    'Holborn': (11.7, 4),
}

# Adjust positions for labels to move them below the nodes
label_positions = {station: (x, y - 0.3) for station, (x, y) in positions.items()}

# Adding edges with actual distances
distances = {
    ('Hyde Park Corner', 'Green Park'): 0.3,
    ('Green Park', 'Piccadilly Circus'): 0.8,
    ('Piccadilly Circus', 'Leicester Square'): 0.4,
    ('Leicester Square', 'Covent Garden'): 0.7,
    ('Covent Garden', 'Holborn'): 1.4
}

# Add the edges to the graph
for edge, distance in distances.items():
    G.add_edge(edge[0], edge[1], weight=distance)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos=positions, with_labels=False, node_size=500, node_color='lightblue')

# Draw labels with adjusted positions below the nodes
nx.draw_networkx_labels(G, pos=label_positions, font_size=10, font_family='sans-serif')

# Draw edge labels (distances)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels)

plt.title("Graph Representation with Labels Below the Nodes")
plt.show()
