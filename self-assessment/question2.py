from collections import deque

# Precedences for operators
pemdas = {
    '+': 1, 
    '-': 1, 
    '*': 2, 
    '/': 2
}

# Tree node class
class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data  
        self.right = right  
        self.left = left  

# Function to convert expression into binary tree
def text_to_tree(expression: str) -> list:
    # Convert expression to list of tokens
    tokens = []
    num = ""
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if char in "+-*/":
                tokens.append(char)
    if num:
        tokens.append(num)


    # Helper function to handle operators and build the tree
    def handle_operator(ops, nums):
        operator = ops.pop()  
        right_node = nums.pop() 
        left_node = nums.pop()  
        nums.append(Node(operator, right_node, left_node))  

    ops = []  # stack to store operators
    nums = []  # stack to store numers

    # Iterate through tokens in expression
    for token in tokens:
        if token.isdigit():  # if token is a number, create a node and push to vals
            nums.append(Node(token))
        elif token in pemdas:  # if token is an operator, call helper function
            while (ops and pemdas[ops[-1]] >= pemdas[token]):
                handle_operator(ops, nums)  
            ops.append(token)  # push the current operator onto the stack

    # Handle any remaining operators
    while ops:
        handle_operator(ops, nums)


    # Traverse tree in a breadth-first search to create final list of branches
    root = nums[0]  

    node_queue = deque([root])  # queue for BFS traversal
    visited_nodes = set()  # set to track visited nodes
    result = []  # list to store the result edges

    while node_queue:
        current_node = node_queue.popleft()
        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)

        data = current_node.data
        left_node = current_node.left  
        right_node = current_node.right 

        if left_node:  
            edge = f'"{data}" -> "{left_node.data}" // left'
            result.append(edge)
            node_queue.append(left_node)
        if right_node:
            edge = f'"{data}" -> "{right_node.data}" // right'
            result.append(edge)
            node_queue.append(right_node)

    return result


def print_output(output: list) -> None:
    for line in output:
        print(line)


if __name__ == "__main__":
    expression = "2*7+3"  # Test 1
    output = text_to_tree(expression)
    print_output(output)
    print()
    expression = "8/2*10"  # Test 2
    output = text_to_tree(expression)
    print_output(output)