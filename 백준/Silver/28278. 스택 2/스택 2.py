from collections import deque
import sys

stack = deque([])

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(data) == 2:
        stack.append(data[-1])
    else:
        if data[0] == 2:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif data[0] == 3:
            print(len(stack))
        elif data[0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif data[0] == 5:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])