'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack.pop() != pairs[i]:
                    return False

        return not stack