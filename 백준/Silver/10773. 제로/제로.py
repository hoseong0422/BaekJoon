import sys
N = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(N):
    I = int(sys.stdin.readline().rstrip())
    if I != 0:
        lst.append(I)
    else:
        lst = lst[:-1] 
print(sum(lst))