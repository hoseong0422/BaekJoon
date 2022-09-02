case = int(input())

for i in range(case):
    custom_cnt = 0
    H, W, N = map(int, input().split())
    
    # 층을 손님 수로 나눈 나머지가 마지막 손님이 가게될 층
    # N / H의 나머지가 0이라면 손님은 H층으로 가게 된다.
    if N % H == 0:
        floor = H
        room= N // H
        
    else:
        floor = N % H
        # N % H가 0이 아니라면 방번호는 손님 수를 층으로 나눈 몫에 1을 더해준다.
        room = N // H + 1

    if len(str(room)) > 1:
        print(f"{floor}{room}")
        
    else:
        print(f"{floor}0{room}")