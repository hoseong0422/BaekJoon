from collections import deque
N = int(input())
queue = deque([i for i in range(1, N+1)])
while True:
    if N == 1:
        print(N)
        break
    elif len(queue) == 2:
        queue.popleft()
        print(queue.popleft())
        break
    queue.popleft()
    queue.append(queue.popleft())