"""
Do not return anything, modify nums1 in-place instead.

- use three pointers
- interate BACKWARDS
- modify IN PLACE

Time: O(m + n)
Space: O(1)


example
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

"""


def merge(nums1, m, nums2, n):
    
    p1 = m - 1
    p2 = n - 1
    
    for p in range(n + m - 1, -1, -1):
        # remember to check out of range pointers are each iteration
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

'''
Tips: Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.
''' 
