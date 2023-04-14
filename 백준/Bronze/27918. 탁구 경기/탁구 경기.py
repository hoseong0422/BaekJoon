N = int(input())
d_cnt = 0
p_cnt = 0
cold = False
for _ in range(N):
    winner = input()
    if winner == 'D':
        d_cnt += 1
    else:
        p_cnt += 1
    if d_cnt - p_cnt == 2 or p_cnt - d_cnt == 2:
        print(f'{d_cnt}:{p_cnt}')
        cold = True
        break
if cold != True:
    print(f'{d_cnt}:{p_cnt}')