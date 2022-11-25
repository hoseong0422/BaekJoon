def solution(n):
    answer = 0
    num = 1
    cnt = 1
    while True:
        if num % 3 == 0 or str(3) in str(num):
            num += 1
            continue
        elif cnt == n:
            return num
        else:
            num += 1
            cnt += 1