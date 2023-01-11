N = int(input())

cnt_0 = 0
cnt_1 = 0
for _ in range(N):
    data = int(input())
    if data == 1:
        cnt_1 += 1
    else:
        cnt_0 += 1
        
if cnt_0 > cnt_1:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
    