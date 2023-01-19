T = int(input())
cnt = 0
for i in range(1, T+1):
    temp = [s for s in str(i)]
    cnt += temp.count('3')
    cnt += temp.count('6')
    cnt += temp.count('9')
print(cnt)