def solution(array):
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            answer = [max, i]
    return answer