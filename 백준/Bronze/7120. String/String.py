data = input()
answer = ''
for i in data:
    if len(answer) == 0:
        answer += i
    elif answer[-1] != i:
        answer += i
print(answer)