N = int(input())
num = 1
for i in range(1, N + 1):
    num *= i
cnt = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    elif i == '0':
        cnt += 1
print(cnt)