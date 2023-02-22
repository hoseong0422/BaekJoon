i = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = n1 // 2
        num = 'even'
    else:
        n2 = (n1 + 1) // 2
        num = 'odd'
    n3 = 3 * n2
    n4 = n3 // 9
    print(f'{i}. {num} {n4}')
    i += 1