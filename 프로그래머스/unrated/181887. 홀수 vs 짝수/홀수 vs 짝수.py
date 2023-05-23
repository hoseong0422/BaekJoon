def solution(num_list):
    odd_sum = 0
    even_sum = 0
    init = 1
    for i in num_list:
        if init % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        init += 1
    if even_sum > odd_sum:
        return even_sum
    elif even_sum < odd_sum:
        return odd_sum
    else:
        return odd_sum