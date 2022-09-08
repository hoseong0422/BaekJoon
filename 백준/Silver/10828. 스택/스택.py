import sys
N = int(sys.stdin.readline().rstrip())
stack = []
stack_top = -1

def push(n):
    global stack_top, stack
    stack_top += 1
    stack.append(n)
    return stack, stack_top

def pop():
    global stack_top, stack
    if stack_top == -1:
        print(-1)
    else:
        print(stack[stack_top])
        stack = stack[:-1]
        stack_top -= 1
    return stack, stack_top

def size():
    global stack
    print(len(stack))
    
def empty():
    global stack_top
    if stack_top == -1:
        print(1)
    else:
        print(0)

def top():
    global stack_top
    if stack_top == -1:
        print(-1)
    else:
        print(stack[stack_top])
        
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    if data.split()[0] == 'push':
        push(int(data.split()[1]))
    elif data == 'pop':
        pop()
    elif data == 'size':
        size()
    elif data == 'empty':
        empty()
    elif data == 'top':
        top()