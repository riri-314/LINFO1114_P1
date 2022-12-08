import numpy as np
import heapq


def dijkstra_all_pairs(graph):
  # Initialize a matrix to store the distances of the shortest paths between all pairs of nodes
  distances = np.full(graph.shape, np.inf)
  
  # Loop over all nodes in the graph
  for start in range(graph.shape[0]):
    # Initialize distances and visited arrays
    distances[start] = np.full(graph.shape[0], np.inf)
    visited = np.zeros(graph.shape[0], bool)
  
    # Set the distance to the start node to be 0
    distances[start][start] = 0
  
    # Create a priority queue to store the nodes to be processed
    # This queue will be sorted by the distance to the node,
    # so that the node with the shortest distance will be processed first
    queue = [(0, start)]
  
    # Loop until the priority queue is empty
    while queue:
      # Get the node with the shortest distance from the queue
      dist, node = heapq.heappop(queue)
    
      # Skip the node if it has already been visited
      if visited[node]:
        continue
      
      # Mark the node as visited
      visited[node] = True
    
      # Update the distances of the neighboring nodes
      for i, d in enumerate(graph[node]):
        if d > 0:  # Check if there is an edge between node and i
          new_dist = dist + d  # Calculate the distance to i through node
          if new_dist < distances[start][i]:  # Check if the new distance is shorter than the current distance
            distances[start][i] = new_dist  # Update the distance to i
            heapq.heappush(queue, (new_dist, i))  # Add i to the queue to be processed
            
  # Return the distances matrix
  return distances

graph = np.array([
  [0, 1, 3],
  [1, 0, 1],
  [3, 1, 0]
])

def read_csv_to_matrix(filename):
    """
    Reads a CSV file containing a costs matrix and returns the
    numpy matrix.
    - integer or float for normal costs
    - inf if no path between the nodes
    :param filename: Path and name of the input file
    :return: Numpy matrix of the costs
    """
    matrix = np.loadtxt(open(filename, "rb"), delimiter=",").astype(float)
    return matrix

matrix = read_csv_to_matrix("graph.csv")
#print(matrix)

print(dijkstra_all_pairs(matrix))