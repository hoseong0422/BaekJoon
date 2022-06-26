def find_han_number():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        # 1부터 99까지는 모든 수가 등차수열에 해당
        if i < 100:
            cnt += 1
        else:
            strN = str(i)           
            # 등차수열 찾기 조건
            if (int(strN[0]) - int(strN[1])) == (int(strN[1]) - int(strN[2])):
                cnt += 1
    print(cnt)
find_han_number()