for i in range(3):
    yut = list(map(int, input().split()))
    yut_cnt = yut.count(0)
    if yut_cnt == 1:
        print('A')
    elif yut_cnt == 2:
        print('B')
    elif yut_cnt == 3:
        print('C')
    elif yut_cnt == 4:
        print('D')
    else:
        print('E')