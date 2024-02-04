a = [int(input()) for _ in range(5)]
set_a = set(a)

answer = 0
for i in set_a:
    if a.count(i) % 2 != 0:
        answer = i
print(answer)