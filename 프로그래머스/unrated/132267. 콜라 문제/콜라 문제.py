def solution(a, b, n):
    answer = 0
    while True:
        if n < a :
            return answer
        changed = (n // a) * b
        answer += changed
        n = changed + (n % a)
