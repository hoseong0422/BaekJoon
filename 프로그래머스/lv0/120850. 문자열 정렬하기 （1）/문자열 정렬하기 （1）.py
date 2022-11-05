def solution(my_string):
    nums = [str(i) for i in range(0, 10)]
    answer = []
    for j in my_string:
        if j in nums:
            answer.append(int(j))
    answer.sort()
    return answer