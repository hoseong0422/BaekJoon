score = [sum(list(map(int, input().split()))) for i in range(5)]
max_score = max(score)
if score.count(max_score) == 1:
    print(f'{score.index(max_score) + 1} {max_score}')