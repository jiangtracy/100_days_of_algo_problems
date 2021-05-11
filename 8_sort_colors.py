'''
use three pointers

- first, second third => start of red, white, blue index
- the second index will be used for looking at every element
- iterate over the array
- if value is 0, swap with current first index
- increase both first and second index by 1
- if value is 1
- increase second index
- otherwise swap with the last index
- decrease last index by 1

leetcode 75

'''


def sort_colors(nums):

    first_idx, second_idx, third_idx = 0, 0, len(nums) - 1

    while second_idx <= third_idx:

        if nums[second_idx] == 0:
            nums[second_idx], nums[first_idx] = nums[first_idx], nums[second_idx]
            first_idx += 1
            second_idx += 1
        elif nums[second_idx] == 1:
            second_idx += 1
        else:
            nums[second_idx], nums[third_idx] = nums[third_idx], nums[second_idx]
            third_idx -= 1

    return nums

