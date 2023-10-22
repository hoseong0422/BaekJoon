N = int(input())
for _ in range(N):
    data = input()
    answer = ''

    for i in data:
        if answer == '':
            answer += i
        elif i != answer[-1]:
            answer += i
    
    print(answer)