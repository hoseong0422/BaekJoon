import sys
deque = []
N = int(sys.stdin.readline())
for _ in range(N):
    data = list(map(str, sys.stdin.readline().split()))
    if data[0] == 'push_front':
        deque = [int(data[1])] + deque
    elif data[0] == 'push_back':
        deque.append(int(data[1]))
    elif data[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque = deque[1:]
    elif data[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque = deque[:-1]
    elif data[0] == 'size':
        print(len(deque))
    elif data[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif data[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])