def solution(slice, n):
    # slice * x / n > 1
    i = 0
    while True:
        if slice * i / n >= 1:
            return i
        i += 1