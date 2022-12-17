def solution(n):
    nums = []
    i = 2
    while n > 1:
        if n % i == 0:
            nums.append(i)
            n = n // i
        else:
            i += 1
    answer = list(set(nums))
    answer.sort()
    return answer