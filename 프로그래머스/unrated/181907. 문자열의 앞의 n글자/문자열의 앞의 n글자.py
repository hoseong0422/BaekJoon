def solution(my_string, n):
    answer = ''
    cnt = 0
    for i in my_string:
        if cnt == n:
            break
        answer += i
        cnt += 1
    return answer