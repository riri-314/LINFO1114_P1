import numpy as np
import heapq

def dijkstra(graph, start):
  # Initialize distances and visited arrays
  distances = np.full(graph.shape[0], np.inf)
  visited = np.zeros(graph.shape[0], np.bool)
  
  # Set the distance to the start node to be 0
  distances[start] = 0
  
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
        if new_dist < distances[i]:  # Check if the new distance is shorter than the current distance
          distances[i] = new_dist  # Update the distance to i
          heapq.heappush(queue, (new_dist, i))  # Add i to the queue to be processed
          
  # Return a matrix of distances from the start node to all other nodes
  return np.array([
    [distances[i] if i != start else 0 for i in range(graph.shape[0])]
  ])

graph = np.array([
  [0, 1, 3],
  [0, 0, 1],
  [1, 0, 0]
])

print(len(graph))

# Find the distances from node 0 to all other nodes
start = 0
distances = dijkstra(graph, start)

print(len(distances))

# Print the distances
for j in range(len(distances)):
    print(distances[j])
#print(distances)