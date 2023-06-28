h, m, s = map(int, input().split(" "))
cook_time = int(input())

cook_second = (cook_time + s) % 60
cook_minute = (m + (cook_time + s) // 60) % 60
cook_hour = h + ((m + ((cook_time + s) //60)) // 60)
cook_hour %= 24
    
print(f"{cook_hour} {cook_minute} {cook_second}")