# leetcode # 112

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursively
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if root is None:
#             return False

#         targetSum -= root.val

#         if root.left is None and root.right is None:
#             return targetSum == 0

#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# iteratively
# in this case, iterative seems to be faster
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        if root is None:
            return False

        stack = [(root, targetSum)]

        # as long as stack is not empty
        while stack:
            node, targetSum = stack.pop()
            targetSum -= node.val

            if not node.left and not node.right and targetSum == 0:
                return True

            if node.left:
                stack.append((node.left, targetSum))

            if node.right:
                stack.append((node.right, targetSum))

        return False

    