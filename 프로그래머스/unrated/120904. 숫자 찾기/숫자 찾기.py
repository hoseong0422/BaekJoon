def solution(num, k):
    cnt = 0
    if str(k) in str(num):
        for i in str(num):
            if i == str(k):
                return (cnt + 1)
            else:
                cnt += 1
    if cnt == 0:
        return -1