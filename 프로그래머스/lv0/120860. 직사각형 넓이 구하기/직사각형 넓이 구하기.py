def solution(dots):
    dots.sort()
    return abs(dots[1][1] - dots[0][1]) * abs(dots[2][0] - dots[0][0])

