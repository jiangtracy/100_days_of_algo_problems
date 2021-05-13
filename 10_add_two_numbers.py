# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Possible edge cases
# two numbers unequal length
# sum has more digits
# Pseudcode
# create a dummy head with a new list node
# have the tail also point at the same dummy head
# create a var to track sum, inilized to be 0
# use a while loop, loop until all the following is false
# l1, l2, sum
# every iteration, add the two numbers, if one doesn't exist use 0
# return the next node of dummy head

# leetcode #2


def addTwoNumbers(l1, l2):
    dummy = tail = ListNode(0)
    list_sum = 0

    while l1 or l2 or list_sum:
        list_sum += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        tail.next = ListNode(list_sum % 10)
        tail = tail.next
        list_sum //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next



