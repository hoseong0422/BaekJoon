N = int(input())

answer = 0

for i in range(1, N + 1):
    if N % i  == 0:
        answer += i

print(answer * 5 - 24)