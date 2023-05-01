str = input()
answer = ''
for i in str:
    if i == i.lower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)
    