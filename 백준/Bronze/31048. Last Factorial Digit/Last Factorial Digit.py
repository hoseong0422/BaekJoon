N = int(input())

for _ in range(N):
    M = int(input())
    answer = 1
    
    for i in range(1, M+1):
        answer *= i
    
    print(str(answer)[-1])