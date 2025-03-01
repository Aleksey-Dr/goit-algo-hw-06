import networkx as nx

G = nx.Graph()

points = [
    "Point A",
    "Point B",
    "Point C",
    "Point D",
    "Point E",
    "Point F"
]
G.add_nodes_from(points)

edges_with_weights = [
    ("Point A", "Point B", 5),
    ("Point B", "Point C", 3),
    ("Point C", "Point D", 4),
    ("Point D", "Point E", 2),
    ("Point E", "Point F", 6),
    ("Point B", "Point D", 7),
    ("Point A", "Point D", 9),
    ("Point C", "Point F", 8)
]
G.add_weighted_edges_from(edges_with_weights)

print("Edges of a graph with weights:")
for u, v, weight in G.edges(data=True):
    print(f"({u}, {v}) -> weight: {weight['weight']}")

# We use Dijkstra's algorithm to find the shortest paths from "Point A" to all other peaks
shortest_paths = nx.single_source_dijkstra_path(G, source="Point A")
shortest_distances = nx.single_source_dijkstra_path_length(
    G, source="Point A"
    )

print("\nThe shortest paths from Point A:")
for target in points:
    print(
        (f"To {target}: way {shortest_paths[target]}, "
         f"distance {shortest_distances[target]}")
    )