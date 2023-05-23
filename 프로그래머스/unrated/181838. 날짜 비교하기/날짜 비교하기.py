def solution(date1, date2):
    if int(''.join([str(i) for i in date1])) < int(''.join([str(i) for i in date2])):
        return 1
    else:
        return 0