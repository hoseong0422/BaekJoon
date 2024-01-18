N = int(input())
S = input()
answer = []
target = 'uospc'
for s in target:
    answer.append(S.count(s))

print(min(answer))