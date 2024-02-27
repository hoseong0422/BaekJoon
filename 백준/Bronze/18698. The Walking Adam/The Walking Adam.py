N = int(input())

for _ in range(N):
    answer = 0

    data = input()
    for d in data:
        if d == 'D':
            break
        else:
            answer += 1
    print(answer)
