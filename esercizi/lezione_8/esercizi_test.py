"""
Es 6:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
write a function to determine if the input string is valid.

An input string is valid if: 

-  Open brackets must be closed by the same type of brackets.
-  Open brackets must be closed in the correct order.
-  Every close bracket has a corresponding open bracket of the same type.
"""

def is_valid_parenthesis(s: str) -> bool:
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or \
                (c == ')' and stack[-1] != '(') or \
                (c == '}' and stack[-1] != '{') or \
                (c == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return not stack

"""
Es 5:
Given a string s which consists of lowercase or uppercase letters, write a function that 
returns the length of the longest palindrome that can be built with those letters. 
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""
