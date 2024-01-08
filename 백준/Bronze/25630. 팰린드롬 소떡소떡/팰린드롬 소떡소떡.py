N = int(input())
N //= 2

data = input()
answer = 0
for i, j in zip(data[:N], data[-1:-N-1:-1]):
    if i != j:
        answer += 1

print(answer)