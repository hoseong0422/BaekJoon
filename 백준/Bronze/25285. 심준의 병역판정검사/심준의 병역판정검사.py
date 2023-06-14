T = int(input())
for _ in range(T):
    height, weight = map(str, input().split(' '))
    height = int(height)
    weight = int(weight)
    BMI = weight / ((height/100) ** 2)
    
    if height > 204 or (height >= 146 and height < 159):
        print(4)
    elif height < 140.1:
        print(6)
    elif height >= 140.1 and height < 146:
        print(5)
    elif height >= 159 and height <161:
        if BMI >= 16.0 and BMI < 35.0:
            print(3)
        else:
            print(4)
    else:
        if BMI >= 20 and BMI < 25:
            print(1)
        elif (BMI >= 18.5 and BMI < 20.0) or (BMI >= 25.0 and BMI < 30.0):
            print(2)
        elif BMI >= 35 or BMI < 16.0:
            print(4)
        else:
            print(3)