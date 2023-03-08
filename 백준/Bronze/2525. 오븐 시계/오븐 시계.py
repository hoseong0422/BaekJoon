H, M = map(int, input().split(" "))
T = int(input())

to_minute = (H * 60) + M
total_minute = to_minute + T

if total_minute == 1440:
    print("0 0")
elif (total_minute // 60) == 24:
    H = 0
    M = total_minute % 60
    print(f"{H} {M}")
elif (total_minute // 60) > 24:
    H = (total_minute // 60) - 24
    M = total_minute % 60
    print(f"{H} {M}")
else:    
    H = total_minute // 60
    M = total_minute % 60
    print(f"{H} {M}")