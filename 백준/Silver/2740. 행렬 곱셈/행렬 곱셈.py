N, M = map(int, input().split())
lst_a = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
lst_b = [list(map(int, input().split())) for _ in range(M)]

lst_c = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            lst_c[i][j] += lst_a[i][k] * lst_b[k][j]
            
for x in lst_c:
    print(*x)