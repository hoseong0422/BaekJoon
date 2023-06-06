def solution(my_string, s, e):
    lst_my_string = [i for i in my_string]
    lst_my_string[s:e+1] = lst_my_string[s:e+1][::-1]
    return ''.join(lst_my_string)