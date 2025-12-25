N = int(input())

length = 1
start = 1
answer = 0

while start <= N:
    end = start * 10 - 1
    end = min(N, end)

    count = end - start + 1
    answer += count * length

    start *= 10
    length += 1

print(answer)