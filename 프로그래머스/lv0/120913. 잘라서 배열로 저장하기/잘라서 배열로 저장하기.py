def solution(my_str, n):
    answer = []
    N = len(my_str) // n + 1
    for i in range(N):
        if len(my_str[:n]) > 0:
            answer.append(my_str[:n])
            my_str = my_str[n:]
    return answer