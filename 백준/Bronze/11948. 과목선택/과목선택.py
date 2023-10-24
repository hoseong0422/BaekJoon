gwatams = []
satams = []

for i in range(6):
    if i < 4:
        gwatams.append(int(input()))
    else:
        satams.append(int(input()))
        
print(sum(gwatams) + sum(satams) - min(gwatams) - min(satams))