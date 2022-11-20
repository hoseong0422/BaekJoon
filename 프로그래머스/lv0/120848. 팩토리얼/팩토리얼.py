def solution(n):
    facto = 1
    cnt = 1
    while True:
        facto = facto * cnt
        if facto == n:
            return cnt
        elif facto > n:
            return cnt - 1
        cnt += 1
        