J, N = map(int, input().split())
answer = 0

for _ in range(N):
    data = input()
    temp = 0
    for i in data:
        if i.isdigit():
            temp += 2
        elif i == ' ':
            temp += 1    
        elif i.upper() == i:
            temp += 4
        else:
            temp += 2
    if temp <= J:
        answer += 1
print(answer)