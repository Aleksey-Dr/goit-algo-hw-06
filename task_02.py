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

edges = [("Point A", "Point B"), ("Point B", "Point C"),
         ("Point C", "Point D"), ("Point D", "Point E"),
         ("Point E", "Point F"), ("Point B", "Point D"),
         ("Point A", "Point D"), ("Point C", "Point F")]
G.add_edges_from(edges)

# path from Point A to Point F using DFS
def dfs_path(graph, start, target):
    predecessors = nx.dfs_predecessors(graph, start)
    path = [target]
    while target in predecessors:
        target = predecessors[target]
        path.append(target)
    return path[::-1]

dfs_path_result = dfs_path(G, "Point A", "Point F")
print("The way with help DFS:", dfs_path_result)

# path from Point A to Point F using BFS
bfs_path = list(
    nx.shortest_path(G, source="Point A", target="Point F")
    )
print("The way with help BFS:", bfs_path)