def solution(my_string, index_list):
    answer = ''
    data = [i for i in my_string]
    for idx in index_list:
        answer += data[idx]
    return answer