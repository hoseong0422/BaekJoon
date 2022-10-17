def solution(n):
    even = '수박'
    odd = '수'
    if n % 2 == 0:
        return even * (n  // 2)
    else:
        return even * (n // 2) + odd