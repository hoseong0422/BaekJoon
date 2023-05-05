def solution(num_list):
    gop = 1
    for i in num_list:
        gop *= i
    if gop > sum(num_list)**2:
        return 0
    else:
        return 1