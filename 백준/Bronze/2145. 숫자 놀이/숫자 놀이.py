while True:
    N = str(input())
    if N == "0":
        break
    if len(N) == 1:
        print(N)
    else:
        while True:
            if len(N) == 1:
                break
            N = str(sum([int(i) for i in N]))
        print(N)