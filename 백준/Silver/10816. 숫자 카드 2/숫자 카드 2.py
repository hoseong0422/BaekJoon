import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
hash_dict = {}
for i in range(N):
    if data[i] in hash_dict.keys():
        hash_dict[data[i]] = hash_dict[data[i]] + 1
    else:
        hash_dict[data[i]] = 1

M = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))
answer = []

for j in find:
    if j in hash_dict.keys():
        answer.append(hash_dict[j])
    else:
        answer.append(0)
print(*answer, sep=' ')