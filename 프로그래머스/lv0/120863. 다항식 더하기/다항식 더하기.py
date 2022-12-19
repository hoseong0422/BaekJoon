def solution(polynomial):
    cnt_x = 0
    cnt_num = 0
    data = polynomial.split()
    for i in data:
        if i == '+':
            continue
        elif i[-1] == 'x':
            if len(i) == 1:
                cnt_x += 1
            else:
                cnt_x += int(i[:-1])
        else:
            cnt_num += int(i)
    if cnt_num == 0:
        if cnt_x == 1:
            return 'x'
        else:
            
            return f'{str(cnt_x)}x'
    elif cnt_x == 0:
        return str(cnt_num)
    else:
        if cnt_x == 1:
            return f'x + {str(cnt_num)}'
        else:
            return f'{str(cnt_x)}x + {str(cnt_num)}'