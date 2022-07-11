data = str(input())
init = len(data)
for i in range(len(data)):
    if data[i:i+2] in ("c=", "c-", "d-", "lj", "nj", "s="):
        init -= 1
    elif data[i:i+2] == "z=":
        if data[i-1:i+2] == "dz=":
            init -= 2
        else:
            init -= 1
print(init)
