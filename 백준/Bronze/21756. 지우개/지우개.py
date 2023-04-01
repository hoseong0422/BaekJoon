N = int(input())
data = [i for i in range(1, N+1)]
while True:
    if len(data) == 1:
        print(data[0])
        break
    del_idx = [i for i in range(1, len(data)+1) if i % 2 != 0]
    del_num = [data[i-1] for i in del_idx]
    for i in del_num:
        data.remove(i)