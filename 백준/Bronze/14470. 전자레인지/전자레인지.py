A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    answer = (A * -1) * C + D + (B * E)
elif A == 0:
    answer = D + (B * E)
else:
    answer = (B - A) * E


print(answer)