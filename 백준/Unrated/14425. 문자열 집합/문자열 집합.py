N, M = map(int, input().split())
S = [input() for i in range(N)]
str_lst = [input() for i in range(M)]
cnt = 0
for i in str_lst:
    if i in S:
        cnt += 1
print(cnt)