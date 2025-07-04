def facto(N, answer):
    if N == 0:
        print(answer)

    elif N >= 2:
        answer *= N
        facto(N - 1, answer)
    
    else:
        print(answer)

N = int(input())
answer = 1
facto(N, answer)