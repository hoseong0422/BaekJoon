N = int(input())
for _ in range(N):
    Y, K = (0, 0)
    for _ in range(9):
        Y_score, K_score = map(int, input().split())
        Y += Y_score
        K += K_score
        
    if Y > K:
        print('Yonsei')
    elif Y == K:
        print('Draw')
    else:
        print('Korea')