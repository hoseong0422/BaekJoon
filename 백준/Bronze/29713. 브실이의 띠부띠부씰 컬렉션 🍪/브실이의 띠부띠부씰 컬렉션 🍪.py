S = 'BRONZESILV' 
N = int(input())
data = input()

answer = []
for s in S:
    if s == 'R' or s == 'E':
        answer.append(data.count(s) // 2)
    else:
        answer.append(data.count(s))

print(min(answer))