N = int(input())
answer = []

for i in range(N):
    data = input().split()
    age = int(data[0])
    name = data[1]
    order = i
    answer.append([age, name, i])

answer.sort(key = lambda x : (x[0], x[2]))

for an in answer:
    print(f'{an[0]} {an[1]}')