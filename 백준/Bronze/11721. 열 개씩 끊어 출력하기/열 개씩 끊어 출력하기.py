import math
data = input()
first = 0
last = 10
N = math.ceil(len(data) / 10)

for i in range(N):
    print(data[first:last])
    first = last
    last += 10