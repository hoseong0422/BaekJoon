A = input()
data = map(str, input().split())
for i in data:
    lower_i = i.lower()
    A = A.replace(i, lower_i)
print(A)