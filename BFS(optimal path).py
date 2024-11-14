# Define the graph as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8', '9'],
    '2': [],
    '4': ['8','6'],
    '8': [],
    '9': [],
  '6': []  # Define '6' with an empty list as its neighbors

}

# Define the BFS function to find and display all paths from start to any reachable node
def bfs_all_paths(graph, start):
    # Initialize the queue with paths starting from the start node
    queue = [[start]]

    print("ALL POSSIBLE PATHS FROM", start, ":")

    # Traverse the graph to find all paths
    while queue:
        # Get the first path from the queue
        path = queue.pop(0)
        # Get the last node in the current path
        node = path[-1]

        # If the node has no unvisited neighbors, print the current path as complete
        if not graph[node]:
            print(" -> ".join(path))

        # For each neighbor, create new paths and add to the queue
        for neighbour in graph[node]:
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)

# Call the BFS function with the start node '5'
bfs_all_paths(graph, '5')
