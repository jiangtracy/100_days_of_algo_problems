'''
- create a dictionary to store numbers already looked
through and its corresponding index
- loop over the array
- at each iteration, first calculate the number needed to add up to target
- if that number already exist in the dictionary, return both indices
- otherwise save the current element and index to dictionary

leetcode #1
'''


def twoSum(nums, target):
        
    numsAppeared = {}
        
    for i in range(0, len(nums)):
        num = nums[i]
        targetNum = target - num
        
        if numsAppeared.get(targetNum) is not None:
            return [i, numsAppeared[targetNum]]
        else:
            numsAppeared[num] = i

