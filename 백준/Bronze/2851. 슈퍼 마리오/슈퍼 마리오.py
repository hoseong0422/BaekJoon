total = 0
for _ in range(10):
    mush = int(input())
    if total + mush == 100:
        total += mush
        break
    elif total + mush < 100: 
        total += mush
    else:
        if total + mush - 100 < 100 - total:
            total += mush
            break
        elif total + mush - 100 == 100 - total:
            total += mush
            break
        else:
            break
print(total)