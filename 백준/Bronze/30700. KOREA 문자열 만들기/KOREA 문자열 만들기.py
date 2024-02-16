target = ['K', 'O', 'R', 'E', 'A']
now = 0
answer = 0

data = input()

for d in data:
    if d == target[now]:
        answer += 1
        if d == 'A':
            now = 0
        else:
            now += 1

print(answer)