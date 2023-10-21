import string

upper_alpha = list(string.ascii_uppercase)

target = 'ILOVEYONSEI'
idx = upper_alpha.index(input())
answer = 0

for i in target:
    if upper_alpha.index(i) < idx:
        answer += idx - upper_alpha.index(i)
        idx = upper_alpha.index(i)
    elif upper_alpha.index(i) > idx:
        answer += upper_alpha.index(i) - idx
        idx = upper_alpha.index(i)

print(answer)