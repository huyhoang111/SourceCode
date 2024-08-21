import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

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

# Define edges and distances (in km)
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

# Extracting data from the graph
total_length = sum(nx.get_edge_attributes(G, 'weight').values())
average_distance = np.mean(list(nx.get_edge_attributes(G, 'weight').values())) #the average distance
std_dev_distance = np.std(list(nx.get_edge_attributes(G, 'weight').values())) #standard deviation

# Output the results
print(f"Total length of the transport network: {total_length:.2f} miles")
print(f"Average distance between the stations: {average_distance:.2f} miles")
print(f"Standard deviation of the distances between the stations: {std_dev_distance:.2f} miles")
