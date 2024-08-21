import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()

# Define positions of all stations
positions = {
    # Line 1 (Blue)
    'Hyde Park Corner': (5.2, 1.7),
    'Green Park': (5.6, 2),
    'Piccadilly Circus': (7.2, 2),
    'Leicester Square': (8, 2),
    'Covent Garden': (9.2, 3),
    'Holborn': (11.7, 4),

    # Line 2 (Red)
    'Euston': (9, 7.4),
    'Warren Street': (8, 6.2),
    'Goodge Street': (8, 5),
    'Tottenham Court Road': (8, 4),
    'Leicester Square': (8, 2),
    'Charing Cross': (8, 1),

    # Line 3 (Green)
    'Paddington': (1.6, 6),
    'Edgware Road': (2.8, 6),
    'Marylebone': (5.4, 6),
    'Oxford Circus': (4, 4),
    'Piccadilly Circus': (7.2, 2),
    'Charing Cross': (8, 1),

    # Line 4 (Yellow)
    'Marble Arch': (3.2, 4),
    'Bond Street': (5.4, 4),
    'Oxford Circus': (6.4, 4),  # Interchange with Green Line
    'Tottenham Court Road': (8, 4),
    'Holborn': (11.2, 4),
    'Chancery Lane': (12.6, 4)
}

# Adjust positions for labels (move them slightly below the nodes, except Oxford Circus and Piccadilly Circus)
label_positions = {station: (x, y - 0.3) for station, (x, y) in positions.items()}

# Adjust the position of "Oxford Circus" and "Piccadilly Circus" to be above the stations
label_positions['Oxford Circus'] = (positions['Oxford Circus'][0], positions['Oxford Circus'][1] + 0.3)
label_positions['Piccadilly Circus'] = (positions['Piccadilly Circus'][0], positions['Piccadilly Circus'][1] + 0.3)

# Define edges and distances (in miles)
distances = {
    # Line 1 (Blue)
    ('Hyde Park Corner', 'Green Park'): 0.3,
    ('Green Park', 'Piccadilly Circus'): 0.8,
    ('Piccadilly Circus', 'Leicester Square'): 0.4,
    ('Leicester Square', 'Covent Garden'): 0.7,
    ('Covent Garden', 'Holborn'): 1.4,

    # Line 2 (Red)
    ('Euston', 'Warren Street'): 0.9,
    ('Warren Street', 'Goodge Street'): 0.5,
    ('Goodge Street', 'Tottenham Court Road'): 0.4,
    ('Tottenham Court Road', 'Leicester Square'): 0.8,
    ('Leicester Square', 'Charing Cross'): 0.5,

    # Line 3 (Green)
    ('Paddington', 'Edgware Road'): 0.6,
    ('Edgware Road', 'Marylebone'): 1.3,
    ('Marylebone', 'Oxford Circus'): 0.8,
    ('Oxford Circus', 'Piccadilly Circus'): 0.8,
    ('Piccadilly Circus', 'Charing Cross'): 0.6,

    # Line 4 (Yellow)
    ('Marble Arch', 'Bond Street'): 1.1,
    ('Bond Street', 'Oxford Circus'): 0.5,
    ('Oxford Circus', 'Tottenham Court Road'): 0.8,
    ('Tottenham Court Road', 'Holborn'): 1.6,
    ('Holborn', 'Chancery Lane'): 0.7
}

# Add the edges to the graph with corresponding distances
for edge, distance in distances.items():
    G.add_edge(edge[0], edge[1], weight=distance)

# Draw the graph with different colors for each line
plt.figure(figsize=(12, 10))

# Colors for each line
colors = ['blue', 'red', 'green', 'yellow']

# Draw each line separately
# Line 1 (Blue)
nx.draw_networkx_edges(G, pos=positions, edgelist=[
    ('Hyde Park Corner', 'Green Park'),
    ('Green Park', 'Piccadilly Circus'),
    ('Piccadilly Circus', 'Leicester Square'),
    ('Leicester Square', 'Covent Garden'),
    ('Covent Garden', 'Holborn')
], edge_color=colors[0], width=2)

# Line 2 (Red)
nx.draw_networkx_edges(G, pos=positions, edgelist=[
    ('Euston', 'Warren Street'),
    ('Warren Street', 'Goodge Street'),
    ('Goodge Street', 'Tottenham Court Road'),
    ('Tottenham Court Road', 'Leicester Square'),
    ('Leicester Square', 'Charing Cross')
], edge_color=colors[1], width=2)

# Line 3 (Green)
nx.draw_networkx_edges(G, pos=positions, edgelist=[
    ('Paddington', 'Edgware Road'),
    ('Edgware Road', 'Marylebone'),
    ('Marylebone', 'Oxford Circus'),
    ('Oxford Circus', 'Piccadilly Circus'),
    ('Piccadilly Circus', 'Charing Cross')
], edge_color=colors[2], width=2)

# Line 4 (Yellow)
nx.draw_networkx_edges(G, pos=positions, edgelist=[
    ('Marble Arch', 'Bond Street'),
    ('Bond Street', 'Oxford Circus'),
    ('Oxford Circus', 'Tottenham Court Road'),
    ('Tottenham Court Road', 'Holborn'),
    ('Holborn', 'Chancery Lane')
], edge_color=colors[3], width=2)

# Draw nodes
nx.draw_networkx_nodes(G, pos=positions, node_size=500, node_color='lightblue')

# Draw labels with adjusted positions
nx.draw_networkx_labels(G, pos=label_positions, font_size=10, font_family='sans-serif')

# Draw edge labels (distances)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels)

# Set plot title
plt.title("London Station Graph(miles)")
plt.show()
