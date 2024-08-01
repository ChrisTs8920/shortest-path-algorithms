import heapq # Implements a heap queue (priority queue)
import time

def dijkstra(graph, source):
    # Priority queue to store the minimum distance to each node
    queue = []
    heapq.heappush(queue, (0, source)) # (distance, node)

    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Dictionary to store the path
    previous_nodes = {node: None for node in graph}

    while queue: # while queue not empty
        current_distance, current_node = heapq.heappop(queue)

        # Nodes can get added to the priority queue multiple times.
        # We only process a node the first time we remove it from the priority queue.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, previous_nodes


def floyd_warshall(graph):
    # List of all vertices
    vertices = list(graph.keys())

    # Initialize the minimum distances matrix with infinities
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}
    
    # Initialize the distances based on the graph edges
    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight
    
    # Distance from each vertex to itself is 0
    for v in vertices:
        dist[v][v] = 0
    
    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


def bellman_ford(graph, source):
    # Initialize predecessors
    previous_nodes = {vertex: None for vertex in graph}

    # Step 1: Initialize distances from source to all other vertices as infinity
    distance = {vertex: float('inf') for vertex in graph}
    distance[source] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    previous_nodes[v] = u
    
    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative weight cycle.")
    
    return distance, previous_nodes


# Helper function to reconstruct the path from source to dest
def reconstruct_path(previous_nodes, source, dest):
    path = []
    current_node = dest
    while current_node != source:
        if current_node is None:
            return None # No path found
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.append(source)
    path.reverse()
    return path


def main():
    # Graphs are represented as a dictionary of dictionaries

    # Example 1
    '''graph = { # undirected graph
        'A': {'B': 1, 'C': 4}, # For example, A is adjacent to B (weight = 1) and C (weight = 4)
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    source_node = 'A'
    dest_node = 'D'
    '''
    # Example 2
    graph = { # directed graph
        'A': {'B': 3, 'C': 2}, # For example, A is adjacent to B (weight = 3) and C (weight = 2)
        'B': {'C': 1, 'D': 4},
        'C': {'D': 2, 'E': 3},
        'D': {'E': 2},
        'E': {'F': 2},
        'F': {'D': 1}
    }
    source_node = 'A'
    dest_node = 'F'

    # DIJKSTRA'S
    print("\nDIJKSTRA'S")
    start = time.time()
    distances, previous_nodes = dijkstra(graph, source_node)
    end = time.time()
    path = reconstruct_path(previous_nodes, source_node, dest_node) # In case we are only interested in a shortest path between source and dest nodes
    print(f"Shortest distances from {source_node}: {distances}")
    print(f"Path from {source_node} to {dest_node}: {path}")
    print("Execution time: ", (round(end - start) * 1000), "ms")

    # FLOYD-WARSHALL
    print("\nFLOYD-WARSHALL")
    start = time.time()
    distances = floyd_warshall(graph)
    end = time.time()
    print("All-pairs shortest distances:")
    for u in distances:
        for v in distances[u]:
            print(f"Distance from {u} to {v} is {distances[u][v]}")
    print("Execution time: ", round((end - start) * 1000), "ms")
    
    # BELLMAN - FORD
    print("\nBELLMAN-FORD")
    try:
        start = time.time()
        distances, previous_nodes = bellman_ford(graph, source_node)
        end = time.time()
        path = reconstruct_path(previous_nodes, source_node, dest_node)
        print(f"Shortest distances from {source_node}: {distances}")
        print(f"Path from {source_node} to {dest_node}: {path}")
        print("Execution time: ", round((end - start) * 1000), "ms")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()