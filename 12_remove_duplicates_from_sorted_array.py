# leetcode 26

# use two pointers, left and right
# whenever the elements are different
# add one to left pointer, then swap value
# then increase right pointer by 1
# return left pointer plus one => length

def remove_duplicates(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[left] != nums[right]:
            # when the elements are different, add one to left index, and then swap value
            left += 1
            nums[left] = nums[right]

        right += 1

    return left + 1