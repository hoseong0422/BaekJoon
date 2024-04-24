N = int(input())
data = [str(input()) for _ in range(N)]

cnt = 0
for d in data:
    if '01' in d or 'OI' in d:

        cnt += 1
print(cnt)