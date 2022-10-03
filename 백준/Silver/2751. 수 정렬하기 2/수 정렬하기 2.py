import sys
N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.sort()
for i in arr:
    print(i)