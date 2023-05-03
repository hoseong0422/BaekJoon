def solution(num_list):
    odd_num = ''
    even_num = ''
    for i in num_list:
        if i % 2 == 0:
            even_num += str(i)
        else:
            odd_num += str(i)
    return int(odd_num) + int(even_num)