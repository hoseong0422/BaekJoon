N = int(input())
data = list(map(int, input().split(" ")))
data.sort()

M = data[N-1]
score_list = []
for d in data:
    score = (d / M) * 100
    score_list.append(score)

sum_score = sum(score_list)
avg = sum_score / N
    
print(avg)