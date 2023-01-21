import sys
N = int(sys.stdin.readline())
M = [int(sys.stdin.readline()) for _ in range(N)]
print(sum(M) - (len(M)-1))
    