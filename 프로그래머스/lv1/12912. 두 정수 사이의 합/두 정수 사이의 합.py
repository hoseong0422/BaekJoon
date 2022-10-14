def solution(a, b):
    if a > b:
        answer = [i for i in range(b, a+1)]
    else:
        answer = [i for i in range(a, b+1)]
    return sum(answer)