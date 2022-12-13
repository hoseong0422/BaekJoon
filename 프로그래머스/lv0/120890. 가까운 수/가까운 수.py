def solution(array, n):
    array.sort()
    answer = 0
    min = n + 100
    for i in array:
        if abs(i - n) < min:
            print(i)
            min = abs(i - n)
            answer = i
    return answer