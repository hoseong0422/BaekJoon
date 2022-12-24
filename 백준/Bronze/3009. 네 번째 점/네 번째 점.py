data = []
for i in range(3):
    data.append(list(map(int, input().split())))
x = []
y = []    
for i in data:
    x.append(i[0])
    y.append(i[-1])
set_x = list(set(x))
set_y = list(set(y))

answer = []
for i in set_x:
    if x.count(i) == 1:
        answer.append(str(i))
        break

for i in set_y:
    if y.count(i) == 1:
        answer.append(str(i))
        break
        
print(' '.join(answer))