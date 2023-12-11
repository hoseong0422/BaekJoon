N = int(input())
answer = ''

for i in range(N):
    input_data = input()
    lst_data = [i for i in input_data]
    if i == 0:
        answer = lst_data[:]
        continue
    else:
        for j in range(len(answer)):
            if answer[j] == '?':
                continue
            elif lst_data[j] != answer[j]:
                answer[j] = '?'

print(''.join(answer))