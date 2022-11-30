def solution(num, total):
    answer = []
    for i in range(-100, total+1):
        arr = [i for i in range(i, i+num)]
        if sum(arr) == total:
            return arr