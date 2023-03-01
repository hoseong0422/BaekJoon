T = int(input())
for _ in range(T):
    N = int(input())
    answer = 0
    for i in range(N+1):
        if i % 2 != 0:
            answer += i
    print(answer)