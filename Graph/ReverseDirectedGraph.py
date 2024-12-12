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