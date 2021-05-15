# This is the class of the input root. Do not edit it.
class binary_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    sums = []
    calc_branch_sum(root, 0, sums)
    return sums


# side effect of this recursive function will append to sums
# this is the helper function to visit all the nodes
def calc_branch_sum(node, branch_sum, sums):
    if node is None:
        return

    branch_sum = branch_sum + node.value

    if node.left is None and node.right is None:
        sums.append(branch_sum)
        return

    # recursively calculate left branch sum and right branch sum
    calc_branch_sum(node.left, branch_sum, sums)
    calc_branch_sum(node.right, branch_sum, sums)


# time: O(n) => we will need to visit all the nodes once
# space: O(n/2) roughly because for every new level
# multiply current nodes count by 2
    # => O(n)


