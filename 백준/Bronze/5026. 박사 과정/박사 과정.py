N = int(input())
for _ in range(N):
    data = input()
    if data == 'P=NP':
        print('skipped')
    else:
        answer = data.split('+')
        print(int(answer[0]) + int(answer[1]))