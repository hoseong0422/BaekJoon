while True:
    stack = []
    data = input()
    if data == '.':
        break
    for i in data:
        if i == '.':
            if len(stack) == 0:
                print('yes')
            else:
                print('no')
        elif i == '[' or i == '(':
            stack.append(i)
        elif i == ']': 
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
        elif i == ')':
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break