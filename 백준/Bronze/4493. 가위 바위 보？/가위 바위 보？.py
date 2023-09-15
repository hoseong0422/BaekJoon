t = int(input())
for _ in range(t):
    n = int(input())
    P1_point = 0
    P2_point = 0
    for _ in range(n):
        P1, P2 = map(str, input().split())
        if P1 == P2:
            P1_point += 1
            P2_point += 1
        elif P1 == 'R':
            if P2 == 'P':
                P2_point += 1
            else:
                P1_point += 1
        elif P1 == 'S':
            if P2 == 'R':
                P2_point += 1
            else:
                P1_point += 1
        else: # P일 때
            if P2 == 'S':
                P2_point += 1
            else:
                P1_point += 1
    if P1_point == P2_point:
        print('TIE')
    elif P1_point > P2_point:
        print('Player 1')
    else:
        print('Player 2')