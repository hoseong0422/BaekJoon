data = input()
a_score = 0
b_score = 0

for i in range(len(data)):
    if i % 2 == 0:
        team = data[i]
    else:
        score = int(data[i])
    
        if team == 'A':
            a_score += score
        else:
            b_score += score

if a_score > b_score:
    print('A')
else:
    print('B')