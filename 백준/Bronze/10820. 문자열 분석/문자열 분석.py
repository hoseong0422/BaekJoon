while True:
    try:
        data = input()
    except EOFError:
        break
    lower_cnt = 0
    upper_cnt = 0
    num_cnt = 0
    blank_cnt = 0

    for i in data:
        if i.isdigit():
            num_cnt += 1
        elif i.isspace():
            blank_cnt += 1
        elif i.isupper():
            upper_cnt += 1
        else:
            lower_cnt += 1
    print(f'{lower_cnt} {upper_cnt} {num_cnt} {blank_cnt}')