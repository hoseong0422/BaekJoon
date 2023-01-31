import sys
a, b= map(int, sys.stdin.readline().rstrip().split())
n1 = min(a, b)
n2 = max(a, b)
data = [i for i in range(n1+1, n2)]
print(len(data))
print(*data, sep=' ')
