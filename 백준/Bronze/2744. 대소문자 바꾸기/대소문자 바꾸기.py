a = input()
answer = ''
for i in range(len(a)):
    if a[i] == a[i].lower():
        answer += a[i].upper()
    else:
        answer += a[i].lower()
print(answer)