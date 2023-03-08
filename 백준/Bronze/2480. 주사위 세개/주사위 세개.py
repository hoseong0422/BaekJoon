data = list(map(int, input().split(" ")))
data.sort()

A = data[0]
B = data[1]
C = data[2]

if A == B == C:
    print(10000 + (A * 1000))

elif A == B or A == C:
    print(1000 + (A * 100))

elif B == C:
    print(1000 + (B * 100))

else:
    print(C * 100)