import numpy as np

def Floyd_Warshall(graph):
    num_nodes = np.shape(graph)[0] 
    # Initialize distance matrix 
    dist = np.array(graph)
    # Add intermediate nodes to paths
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])
    return dist

