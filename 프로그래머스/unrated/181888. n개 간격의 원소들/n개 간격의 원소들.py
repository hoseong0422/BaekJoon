def solution(num_list, n):
    answer = []
    i = 0
    while True:
        answer.append(num_list[i])
        if i + n > len(num_list)-1:
            break
        else:
            i += n
    return answer