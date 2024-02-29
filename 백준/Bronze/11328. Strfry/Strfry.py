N = int(input())

for _ in range(N):
    str_1, str_2 = map(str, input().split())
    
    lst_1 = [i for i in str_1]
    lst_1.sort()
    lst_2 = [i for i in str_2]
    lst_2.sort()

    if lst_1 == lst_2:
        print('Possible')
    else:
        print('Impossible')