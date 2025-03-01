import networkx as nx
import matplotlib.pyplot as plt

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

edges = [("Point A", "Point B"), ("Point B", "Point C"),
         ("Point C", "Point D"), ("Point D", "Point E"),
         ("Point E", "Point F"), ("Point B", "Point D"),
         ("Point A", "Point D"), ("Point C", "Point F")]
G.add_edges_from(edges)

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    font_weight='bold',
    node_size=4000
    )
plt.title("City transport network")
plt.show()

# Graph characteristics analysis
print("Number of vertices:", G.number_of_nodes())
print("Number of ribs:", G.number_of_edges())
print("Vertex degrees:", dict(G.degree()))