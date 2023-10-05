a = 'MOBIS'
b = input()
answer = 0

for i in list(set([i for i in b])):
    if i in a:
        answer += 1
if answer == 5:
    print('YES')
else:
    print('NO')