data = input()
answer = []
for d in data:
    if d.isdigit():
        answer.append(int(d))
if sum(answer[:2]) == answer[-1]:
    print('YES')
else:
    print('NO')