cnt = 0
while True:
    a, b, c = map(str, input().split())
    if b == 'E':
        break
    cnt += 1
    a = int(a)
    c = int(c)
    
    if b == '>':
        if a > c:
            print(f'Case {cnt}: true')
        else:
            print(f'Case {cnt}: false')
    elif b == '>=':
        if a >= c:
            print(f'Case {cnt}: true')
        else:
            print(f'Case {cnt}: false')
    elif b == '<':
        if a < c:
            print(f'Case {cnt}: true')
        else:
            print(f'Case {cnt}: false')
    elif b == '<=':
        if a <= c:
            print(f'Case {cnt}: true')
        else:
            print(f'Case {cnt}: false')
    elif b == '==':
        if a == c:
            print(f'Case {cnt}: true')
        else:
            print(f'Case {cnt}: false')
    elif b == '!=':
        if a != c:
            print(f'Case {cnt}: true')
        else:
            print(f'Case {cnt}: false')