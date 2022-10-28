def solution(my_string, num1, num2):
    lst_my_string = list(my_string)
    temp1 = lst_my_string[num1]
    temp2 = lst_my_string[num2]
    lst_my_string[num1] = temp2
    lst_my_string[num2] = temp1
    
    return ''.join(lst_my_string)