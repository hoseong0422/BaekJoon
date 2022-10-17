def solution(numbers):
    nums = [i for i in range(0, 10)]
    
    return_nums = [i for i in nums if i not in numbers]
    
    answer = sum(return_nums)
    return answer