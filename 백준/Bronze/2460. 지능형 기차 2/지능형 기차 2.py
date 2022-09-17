total = 0
stations = []
for _ in range(10):
    get_off, get_in = map(int, input().split())

    total = total - get_off + get_in
    stations.append(total)

stations.sort()
print(stations[-1])