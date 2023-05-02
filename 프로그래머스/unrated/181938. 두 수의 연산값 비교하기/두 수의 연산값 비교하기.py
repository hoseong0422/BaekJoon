def solution(a, b):
    an_1 = int(str(a) + str(b))
    an_2 = 2 * a * b
    answer = [an_1, an_2]
    answer = list(answer)
    return max(answer)