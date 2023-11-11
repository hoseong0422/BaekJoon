import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

data_dict = {}

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    if len(temp) >= M:
        if temp not in data_dict.keys():
            data_dict[temp] = 1
        else:
            data_dict[temp] += 1

sorted_dict = sorted(data_dict.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))
for i in sorted_dict:
    print(i[0])