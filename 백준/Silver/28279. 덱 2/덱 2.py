from collections import deque
import sys

queue = deque([])

N = int(sys.stdin.readline())
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    if len(data) == 2:
        if data[0] == 1:
            queue.appendleft(data[-1])
        elif data[0] == 2:
            queue.append(data[-1])
    else:
        if data[0] == 3:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
        elif data[0] == 4:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.pop())
        elif data[0] == 5:
            print(len(queue))
        elif data[0] == 6:
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif data[0] == 7:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif data[0] == 8:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])