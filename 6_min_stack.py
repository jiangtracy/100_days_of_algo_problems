"""

pop, top, getMin all needs to be O(1)

- use two stack
- in min_stack, push in a list
- firs element of the list is the number
- second element is how may times it occured

leetcode #155

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val):

        self.stack.append(val)

        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self):

        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1][0]


