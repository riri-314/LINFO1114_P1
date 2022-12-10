import numpy as np

def Bellman_Ford(matrix):
    num_nodes = matrix.shape[0]

    # Initialize distance matrix with infinity values
    distances = np.full((num_nodes, num_nodes), np.inf)

    # Set distance between each node and itself to 0
    for i in range(num_nodes):
        distances[i, i] = 0

    # Iterate over the matrix and update distances
    for i in range(num_nodes):
        for j in range(num_nodes):
            if matrix[i, j] != np.inf:
                distances[i, j] = matrix[i, j]

    # Perform relaxation step num_nodes-1 times
    for k in range(num_nodes-1):
        for i in range(num_nodes):
            for j in range(num_nodes):
                distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    # Check if the graph has negative cycles by looking for
    # distances that can be further relaxed
    for i in range(num_nodes):
        for j in range(num_nodes):
            if distances[i, j] > distances[i, k] + distances[k, j]:
                raise ValueError('Graph contains negative cycle')

    return distances


