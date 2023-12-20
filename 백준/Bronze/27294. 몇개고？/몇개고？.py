T, S = map(int, input().split())


if T >= 12 and T <= 16:
    if S > 0:
        answer = 280
    else:
        answer = 320
else:
    answer = 280

print(answer)