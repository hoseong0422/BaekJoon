A, B, C, M = map(int, input().split())
total_work = 0
fatigue = 0

for i in range(24):
    if fatigue + A > M:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0
    else:
        total_work += B
        fatigue += A
        
print(total_work)