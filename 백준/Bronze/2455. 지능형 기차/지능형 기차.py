passenger = 0
passenger_each_platform = []

for _ in range(4):
    a, b = map(int, input().split())
    passenger += (b - a)
    passenger_each_platform.append(passenger)

passenger_each_platform.sort()
print(passenger_each_platform[-1])