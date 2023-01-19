N, digit = map(int, input().split())

cnt = 0
for i in range(1, N+1):
    temp = [s for s in str(i)]
    cnt += temp.count(str(digit))
print(cnt)