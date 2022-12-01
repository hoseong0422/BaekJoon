def solution(numbers, k):
    if k * 2 > len(numbers):
        return numbers[(k - 1) * 2 % len(numbers)]
    else:
        return numbers[k]