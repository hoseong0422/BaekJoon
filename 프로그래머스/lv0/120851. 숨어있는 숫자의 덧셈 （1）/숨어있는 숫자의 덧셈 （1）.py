def solution(my_string):
    nums = [str(i) for i in range(1, 10)]
    answer = []
    for j in my_string:
        if j in nums:
            answer.append(int(j))
    return sum(answer)