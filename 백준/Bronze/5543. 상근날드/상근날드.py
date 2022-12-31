burgers = [int(input()) for i in range(3)]
beverage = [int(input()) for i in range(2)]

burgers.sort()
beverage.sort()

print(burgers[0] + beverage[0] - 50)