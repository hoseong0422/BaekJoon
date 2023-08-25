N = int(input())
C = 100
S = 100
for _ in range(N):
    c, s = map(int, input().split())
    if c == s:
        continue
    elif c > s:
        S -= c
    else:
        C -= s
print(C, S, sep='\n')