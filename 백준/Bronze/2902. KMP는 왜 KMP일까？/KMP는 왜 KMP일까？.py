data = list(map(str, input().split('-')))
answer = ''
for i in data:
    answer += i[0].upper()
print(answer)