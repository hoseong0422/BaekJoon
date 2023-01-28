N = int(input())
vowels = ['A','E','I','O','U','a','e','i','o','u']
for _ in range(N):
    vowels_cnt = 0
    other = 0
    data = input()
    for i in data:
        if i != " ":
            if i in vowels:
                vowels_cnt += 1
            else:
                other += 1

    print(f'{other} {vowels_cnt}')