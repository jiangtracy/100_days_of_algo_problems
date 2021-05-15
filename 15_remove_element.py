# two pointers
# one start from left, one start front right
# whenever left element needs to be removed, swap with right side

# leetcode 27

def remove_element(nums, val):

    if len(nums) == 0:
        return 0

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1

    # check the element which left and right pointers meet
    # it's possible that element needs to be removed too
    return left + 1 if nums[left] != val else left

# time: O(n) - n is the length of the list
# space: O(1) - in place

# alternatively, can have both pointers start from beginning
