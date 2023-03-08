import sys

T = sys.stdin.readline().rstrip()
T = int(T)
for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split(" "))
    print(A + B)