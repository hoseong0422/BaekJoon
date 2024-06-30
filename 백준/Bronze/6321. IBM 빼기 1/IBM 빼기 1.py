import string  

upper_lst = list(string.ascii_uppercase)
N = int(input())
n = 0

for i in range(N):
    data = input()
    answer = ''
    for d in data:
        if d == 'Z':
            n = 0
        else:
            n = upper_lst.index(d) + 1
        answer += upper_lst[n]
    
    i += 1
    print(f'String #{i}')
    if i != N:
        print(answer+'\n')
    else:
        print(answer)