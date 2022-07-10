data = str(input())
time = 0
for i in data:
    init = 2
    if i in ("A","B","C"):
        init += 1
        time += init
    elif i in ("D","E","F"):
        init += 2
        time += init
    elif i in ("G", "H", "I"):
        init += 3
        time += init
    elif i in ("J", "K", "L"):
        init += 4
        time += init
    elif i in ("M", "N", "O"):
        init += 5
        time += init
    elif i in ("P", "Q", "R", "S"):
        init += 6
        time += init
    elif i in ("T", "U", "V"):
        init += 7
        time += init
    elif i in ("W", "X", "Y", "Z"):
        init += 8
        time += init
print(time)