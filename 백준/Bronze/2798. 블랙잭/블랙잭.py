from itertools import combinations

N, M = map(int, input().split())
max1 = 0
max_list = []

data = list(map(int, input().split()))

combinations_list = list(combinations(data, 3))
for combination in combinations_list:
    combination_max = sum(combination)
    
    if combination_max == M:
        max_list.append(combination_max)
    
    elif combination_max < M:
        if combination_max > max1:
            max1 = combination_max
            max_list.append(max1)

max_list.sort()
print(max_list[-1])