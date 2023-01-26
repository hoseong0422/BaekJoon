import sys
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    data = list(map(str, sys.stdin.readline().split()))
    if data[0] == 'push':
        queue.append(int(data[1]))
    elif data[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:]
    elif data[0] == 'size':
        print(len(queue))
    elif data[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif data[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])