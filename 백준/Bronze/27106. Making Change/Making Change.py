P = int(input())

c_25 = 0
c_10 = 0
c_5 = 0
c_1 = 0

exchange = 100 - P
c_25 += exchange // 25
exchange = exchange % 25
c_10 += exchange // 10
exchange = exchange % 10
c_5 += exchange // 5
exchange = exchange % 5
c_1 += exchange // 1

print(c_25, c_10, c_5, c_1, sep=' ')