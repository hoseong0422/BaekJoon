data = input()
answer = set()

for i in range(len(data)):
    for j in range(i, len(data)):
        temp = data[i:j+1]
        answer.add(temp)

print(len(answer))