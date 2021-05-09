'''
Add two numbers in string format WITHOUT converting to number

input: two string => numbers
output: sume of the two numbers in STRING format

- double pointers methods

- declare a var to save the carryover value
- declare another list var to save current sum (covert to string in the end)
- iterate over both nums, from the back
- convert each to unicode
- subtract the unicode of 0 in string format from it
- check to make sure the index is still greater than 0
- if not, set the corresponding number to int 0
- add two numbers' unicode and carryover, update carryover value
- after the loop, if carryover still exist, add to the list containing sum
- return sum in string format (join reversly!!)

Time O(max(len(num1), len(num2)))
- at most length of the larger number times of iterations
Space O(max(len(num1) + len(num2)) + 1 => at most
- therefore, drop the constant
- O(max(len(num1) + len(num2))

leetcode # 415
'''


def addStrings(self, num1: str, num2: str) -> str:
    sum = []
    i = len(num1) - 1
    j = len(num2) - 1
    carryover = 0
    
    while i >= 0 or j >= 0:
        firstNum = ord(num1[i]) - ord('0') if i >= 0 else 0
        secondNum = ord(num2[j]) - ord('0') if j >= 0 else 0
        
        currentSum = firstNum + secondNum + carryover
        carryover = currentSum // 10 
        currentDigit = currentSum % 10
        sum.append(currentDigit)
        i -= 1
        j -= 1
        
    if carryover > 0:
        sum.append(carryover)

    return ''.join(str(x) for x in sum[::-1])