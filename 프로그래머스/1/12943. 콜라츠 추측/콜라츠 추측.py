def solution(num):
    answer = 0
    while True:
        if answer == 501 and num != 1:
            answer = -1
            break
        if num == 1:
            break
        else:
            if num % 2 == 0:
                num //= 2
                answer += 1
            else:
                num *= 3
                num += 1
                answer += 1
    return answer