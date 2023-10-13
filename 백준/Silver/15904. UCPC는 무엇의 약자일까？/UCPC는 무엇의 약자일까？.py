sentence = input().replace(' ','')
answer = 'UCPC'
idx = 0
for i in sentence:
    if i == answer[idx]:
        idx += 1
    if idx == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')