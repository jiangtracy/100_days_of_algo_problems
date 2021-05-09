'''
input: stirng of brackets
output: true/false

- create stack to keep track of left open brakcets
- everytime we run into a closing braket
- check if it' pairs with the last brackets in the list
- if not return false
- if they pair, pop the last element from the lsit and move on
- return true in the end if nothing is left in brackets list

improvements:
- can also use a hashmap to store bracket pairs
- better than turn into unicode

'''


def isValid(s):
    leftBrackets = '[{('
    # implemented stack with a list
    currentOpenBra = []
    for bracket in s:
        if bracket in leftBrackets:
            currentOpenBra.append(bracket)
        elif not currentOpenBra or ord(bracket) - \
        ord(currentOpenBra[len(currentOpenBra) - 1]) not in range(1, 3):
            return False
        else:
            currentOpenBra.pop()
    
    return not currentOpenBra

# use hashmap when reviewing
