max_cnt = 0
N = int(input())

for _ in range(N):
    data = input()
    temp = 0
    temp += data.count('for')
    temp += data.count('while')

    if temp > max_cnt:
        max_cnt = temp

print(max_cnt)