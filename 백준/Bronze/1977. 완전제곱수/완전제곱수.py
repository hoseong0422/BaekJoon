M = int(input())
N = int(input())
i = 1
answer = []
while True:
    if i ** 2 >= M and i ** 2 <= N:
        answer.append(i ** 2)
    elif i ** 2 > N:
        break
    i += 1
if len(answer) == 0:
    print(-1)
else:
    print(sum(answer), answer[0], sep='\n')