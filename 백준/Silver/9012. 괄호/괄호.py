N = int(input())
for _ in range(N):
    open_cnt = 0
    close_cnt = 0
    PS = input()
    
    if len(PS) % 2 != 0:
        print('NO')
    elif PS[0] == ")" or PS[-1] == '(':
        print('NO')
    elif PS.count('(') == PS.count(')'):
        for i in PS:
            if i == '(':
                open_cnt += 1
            else:
                close_cnt += 1
                if close_cnt > open_cnt:
                    print('NO')
                    break
        if close_cnt == open_cnt:
            print('YES')
    else:
        print('NO')