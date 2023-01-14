m, d = map(int, input().split())
days = 0
for i in range(1, m):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        days += 31
    elif i in [4, 6, 9, 11]:
        days += 30
    else:
        days += 28
days += d

week = 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'
print(week[days%7-1])