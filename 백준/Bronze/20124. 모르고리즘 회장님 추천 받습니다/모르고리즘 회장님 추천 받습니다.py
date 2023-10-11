N = int(input())
names = []
max_score = 0

for _ in range(N):
    name, score = map(str, input().split())
    
    if int(score) == max_score:
        names.append(name)
    elif int(score) > max_score:
        max_score = int(score)
        names = []
        names.append(name)
        
if len(names) == 1:
    print(names[0])
else:
    names.sort()
    print(names[0])