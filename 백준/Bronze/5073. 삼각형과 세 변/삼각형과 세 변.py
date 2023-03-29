while True:
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    if a == b == c == 0:
        break
    # 2개가 같은 경우
    if len(set(lst)) == 1:
        print('Equilateral')
    elif len(set(lst)) == 2:
        sorted(lst)
        if sum(lst[:-1]) > lst[-1]:
            print('Isosceles')
        else:
            print('Invalid')
    elif len(set(lst)) == 3:
        sorted(lst)
        if sum(lst[:-1]) > lst[-1]:
            print('Scalene')
        else:
            print('Invalid')