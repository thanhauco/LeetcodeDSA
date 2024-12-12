# Given a directed graph, reverse the direction of all edges.
# The graph is represented as an adjacency list.    
"""
Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C
"""
def reverse_graph(adj_list):
    # Initialize an empty adjacency list for the reversed graph
    reversed_graph = {node: [] for node in adj_list}
    print("init reversed_graph:", reversed_graph)
    
    # Iterate through each node and its neighbors in the original graph
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            # Reverse the edge direction
            reversed_graph[neighbor].append(node)
    
    return reversed_graph

# Example: Adjacency list representation of a graph
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": []
}

# Compute the reversed graph
reversed_graph = reverse_graph(graph)
print(reversed_graph)

def reverse_graph_edge_list(edge_list):
    """
    Reverse a directed graph represented as an edge list.

    :param edge_list: List of tuples representing edges (u, v)
    :return: Reversed edge list
    """
    # Reverse each edge
    reversed_edges = [(v, u) for u, v in edge_list]
    return reversed_edges

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
print("init edges:", edges)
reversed_edges = reverse_graph_edge_list(edges)
print(reversed_edges)  # Output: [(1, 0), (2, 1), (3, 2), (4, 3)]

"""
If the graph is represented as an adjacency matrix matrix[u][v], where 1 indicates a direct edge, reversing the graph involves transposing the matrix.
"""
def reverse_graph_matrix(adj_matrix):
    """
    Reverse a directed graph represented as an adjacency matrix.

    :param adj_matrix: 2D list representing the adjacency matrix
    :return: Transposed adjacency matrix (reversed graph)
    """
    n = len(adj_matrix)
    reversed_matrix = [[adj_matrix[j][i] for j in range(n)] for i in range(n)]
    return reversed_matrix

# Example usage
adj_matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]
reversed_matrix = reverse_graph_matrix(adj_matrix)
print(reversed_matrix)
# Output: 
# [
#     [0, 0, 1],
#     [1, 0, 0],
#     [0, 1, 0]
# ]