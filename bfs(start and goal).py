# Define the graph as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8', '9'],
    '2': [],
    '4': ['8','6'],
    '8': [],
    '9': [],
    '6': []
}

# Define the BFS function to find a path from start to goal
def bfs_path(graph, start, goal):
    # Initialize visited list and queue, storing each path as a list
    visited = []
    queue = [[start]]  # Queue holds paths, not just nodes

    print("BREADTH FIRST SEARCH PATH:")

    while queue:
        # Get the first path from the queue
        path = queue.pop(0)
        # Get the last node in the path
        node = path[-1]

        # If this node is the goal, return the path
        if node == goal:
            print(" -> ".join(path))
            return

        # If the node hasn't been visited, continue the search
        if node not in visited:
            visited.append(node)
            # Enqueue new paths with each neighbor added
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

# Call the BFS function with start node '5' and goal node '8'
bfs_path(graph, '5', '6')
