def solution(arr, queries):
    answer = []
    for query in queries:
        temp_lst = []
        temp_arr = arr[query[0]:query[1]+1]
        for temp in temp_arr:
            if temp > query[-1]:
                temp_lst.append(temp)
        if len(temp_lst) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp_lst))
    return answer