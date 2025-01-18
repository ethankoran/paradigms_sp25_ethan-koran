# Recursive function to convert a tree structure to text
def tree_to_text(tree, root_node):
    # base case 
    if not tree[root_node]: # if the current node has no children, return its value
        return root_node.split('_')[1]

    # recursively process left and right children to 
    # get expressions from left and right subtrees
    left = tree[root_node][0]
    right = tree[root_node][1]

    left_expr = tree_to_text(tree, left)
    right_expr = tree_to_text(tree, right)

    # parse the operator of current node
    operator = root_node.split('_')[1]

    # return the concatenated string
    return f"{left_expr}{operator}{right_expr}"


if __name__ == "__main__":
    # Test case 1: 2*7+3
    tree =  {"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]}
    root_node = "n1_+" 
    print(tree_to_text(tree, root_node))

    # Test case 2: 3+10/5*2
    tree ={'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []}
    root_node = "n1_+"
    print(tree_to_text(tree, root_node))
