data = input()
vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in data:
    if i in vowels:
        cnt += 1
print(cnt)