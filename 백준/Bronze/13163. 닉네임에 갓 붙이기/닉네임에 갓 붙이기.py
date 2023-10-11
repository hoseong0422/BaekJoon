N = int(input())

for _ in range(N):
    data = list(map(str, input().split()))
    answer = 'god'
    for i in data[1:]:
        answer += i
    print(answer)