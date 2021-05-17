# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def diameter_of_binary_tree(root) :
    diameter = 0

    def longest_path(node):
        if not node:
            return 0

        # make this available to the outer scope
        nonlocal diameter

        left_path = longest_path(node.left)
        right_path = longest_path(node.right)

        # this will be the longest path currently
        diameter = max(left_path + right_path, diameter)

        # 1 is the parent node
        return max(left_path, right_path) + 1

    # start the recursive call
    longest_path(root)

    return diameter

# time: O(n)
# space: O(n), if perfectly balanced, then could be O(logn) in call stack



