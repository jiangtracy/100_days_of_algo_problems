
def product_except_self(nums):
    length = len(nums)
    left_list = [0] * length
    right_list = [0] * length

    # set left product of left most number and right product of right most number to be 1
    left_list[0] = 1
    right_list[len(nums) - 1] = 1

    # get the product of all the numbers to the LEFT of the current element
    for i in range(1, length):
        left_list[i] = nums[i - 1] * left_list[i - 1]

    # get the product of all the numbers to the RIGHT of the current element
    for j in range(length - 2, -1, -1):
        right_list[j] = right_list[j + 1] * nums[j + 1]

    result_list = [0] * length
    for k in range(0, length):
        result_list[k] = left_list[k] * right_list[k]

    return result_list

