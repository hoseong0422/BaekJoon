import sys

N = int(sys.stdin.readline())
answer = set()

for _ in range(N):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            answer = set([i for i in range(1, 21)])
        else:
            answer = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            answer.add(x)
        elif func == "remove":
            answer.discard(x)
        elif func == "check":
            print(1 if x in answer else 0)
        elif func == "toggle":
            if x in answer:
                answer.discard(x)
            else:
                answer.add(x)