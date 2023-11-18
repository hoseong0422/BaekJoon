def solution(arr):
    arr_len = len(arr)

    init = 0
    while True:
        if arr_len == 2 ** init:
            return arr
        elif arr_len > 2 ** init:
            init += 1
        else:
            return arr + [0 for i in range(2 ** init - arr_len)]