from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        
        for parenthese in s:
            if parenthese in "({[":
                stack.append(parenthese)
            elif parenthese == ")":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif parenthese == "}":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif parenthese == "]":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
        
        