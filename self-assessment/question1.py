def bfs_traversal(graph, initial_node):
    # your implementation here

    # initialize queue with root node and visited list
    queue = [initial_node]
    visited = []

    # iterate through queue while queue is not empty
    while queue:
        node = queue.pop(0) # implement FIFO functionality
        if node in visited: # if we have already visited this node, skip
            continue
        visited.append(node)
        # add each node's children to the queue to be processed
        for child in graph[node]: 
            queue.append(child)

    # your function will return a list!
    return visited

if __name__ == "__main__":
    # Test case 1
    graph1 = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    initial_node1 = "+"
    print(bfs_traversal(graph1, initial_node1))
    # Test case 2
    graph2 = {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    initial_node2 = 0
    print(bfs_traversal(graph2, initial_node2))