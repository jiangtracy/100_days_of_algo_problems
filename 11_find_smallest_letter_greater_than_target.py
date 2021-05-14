# leetcode #744 Easy

def next_greatest_letter(letters, target):

    left = 0
    right = len(letters)

    # right index start at out of range because letter wrap around
    # we can then use % to return index 0, if target is greater than all existing character in the array
    while left < right:
        mid = (right + left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    # return index 0 if both left and right land out of the range
    # otherwise will return the current element
    return letters[left % len(letters)]

