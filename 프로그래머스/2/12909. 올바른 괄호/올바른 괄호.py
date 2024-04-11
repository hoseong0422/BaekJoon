def solution(s):
    stack = []    
    if s[0] == ")" or s[-1] == "(":
        return False
    elif s.count('(') == s.count(')'):
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    else:
        return False