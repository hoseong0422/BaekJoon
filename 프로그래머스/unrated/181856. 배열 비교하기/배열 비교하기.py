def solution(arr1, arr2):
    len_1 = len(arr1)
    len_2 = len(arr2)
    if len_1 == len_2:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
    elif len_1 > len_2:
        return 1
    elif len_1 < len_2:
        return -1