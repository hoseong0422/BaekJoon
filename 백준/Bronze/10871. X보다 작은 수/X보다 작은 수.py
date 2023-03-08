N, X = map(int, input().split(" "))

data = list(map(int, input().split(" ")))
lst = []

for i in data:
    if i < X:
        lst.append(lst)
        print(i, end=" ")