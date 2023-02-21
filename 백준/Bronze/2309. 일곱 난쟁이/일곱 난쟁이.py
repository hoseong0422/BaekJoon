from itertools import combinations

data = [int(input()) for i in range(9)]
combi = combinations(data, 7)
for i in combi:
    if sum(list(i)) == 100:
        answer = sorted(i)
        print(*answer, sep='\n')
        break