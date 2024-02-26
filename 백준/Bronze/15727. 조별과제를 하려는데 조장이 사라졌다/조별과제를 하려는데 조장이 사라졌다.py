N = int(input())

answer = 0
if N % 5 == 0:
    answer += N // 5
else:
    answer += ((N // 5) + 1)

print(answer)