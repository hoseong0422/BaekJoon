N = int(input())
students = [str(input()) for _ in range(N)]
temp = []
for i in range(1, len(students[0]) + 1):
    for num in students:
        num = str(num)
        if num[-i:] not in temp:
            temp.append(num[-i:])
        else:
            break
    if len(temp) == N:
        print(i)
        break
    else:
        temp = []
