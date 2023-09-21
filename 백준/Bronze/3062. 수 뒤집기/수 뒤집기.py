N = int(input())
for _ in range(N):
    data = int(input())
    sum_data = data + int(str(data)[::-1])
    if str(sum_data)== str(sum_data)[::-1]:
        print('YES')
    else:
        print('NO')