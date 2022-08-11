N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

answer = 0
A.sort()
for i in range(N):
    X = A[i]
    # B에서 최대값 하나씩 꺼내기
    Y = B.pop(B.index(max(B)))

    answer += X * Y
print(answer)