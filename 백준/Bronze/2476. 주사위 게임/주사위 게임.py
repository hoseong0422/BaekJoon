N = int(input())
max_value = 0
temp_value = 0
for _ in range(N):
    A, B, C = map(int, input().split())
    if A == B == C:
        temp_value = 10000 + A * 1000
    elif A == B:
        temp_value = 1000 + A * 100
    elif A == C:
        temp_value = 1000 + A * 100
    elif B == C:
        temp_value = 1000 + B * 100
    else:
        temp_value = max(A, B, C) * 100
    if temp_value > max_value:
        max_value = temp_value
print(max_value)