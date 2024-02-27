data = input().split('.')

answer = ''
for i in range(len(data)):
    if len(data[i]) % 2 != 0:
        answer = -1
        break

    answer += 'AAAA' * (len(data[i]) // 4)
    answer += 'BB' * (len(data[i]) % 4 // 2)

    if i < len(data) - 1:
        answer += '.'

print(answer)