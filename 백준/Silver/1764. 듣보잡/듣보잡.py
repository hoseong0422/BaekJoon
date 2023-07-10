import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst_1 = []
lst_2 = []
for _ in range(N):
    lst_1.append(input())
for _ in range(M):
    lst_2.append(input())

data = sorted(list(set(lst_1) & set(lst_2)))
print(len(data))
print(''.join(data), end='')