def solution(arr):
    if (len(arr) == 1 and arr[0] == 10) or len(arr) == 0:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr