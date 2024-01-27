target = int(input())
n_2 = 0
n_1 = 1
i = 2
while True:
    now = n_2 + n_1
    i += 1
    n_2 = n_1
    n_1 = now 
    if i > target:
        print(now)
        break