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

# Initialize visited and queue lists
visited = []
queue = []

# Define the BFS function
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    print("BREATH FIRST SEARCH:", end=" ")

    while queue:
        # Dequeue a node from the front of the queue
        m = queue.pop(0)
        print(m, end=" ")

        # Loop through the neighbors of the node
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Call the BFS function starting from node '5'
bfs(visited, graph, '5')
