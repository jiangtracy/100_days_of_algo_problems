# solve recursively
# base case would be root eqaul to none, simply return 0 in this case
# add an extra argument => depth

# average when tree is fairly balanced
# time O(n), n being the number of nodes
# space O(h), h being the height of the tree

def node_depths(root, depth=0):
    # Write your code here.

    if root is None:
        return 0

    return depth + node_depths(root.left, depth + 1) + node_depths(root.right, depth + 1)


# alternatively, can also use a stack to implement
# try it when reviewing

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
