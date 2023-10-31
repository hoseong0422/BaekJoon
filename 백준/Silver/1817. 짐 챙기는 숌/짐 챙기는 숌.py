N, M = map(int, input().split())
if N != 0 :
    books = list(map(int, input().split()))
    weigth = 0
    answer = 1
    for i in range(N-1, -1, -1) :
        weigth += books[i]
        if weigth > M :
            answer += 1
            weigth = books[i]
    print(answer)
else :
    print(0)