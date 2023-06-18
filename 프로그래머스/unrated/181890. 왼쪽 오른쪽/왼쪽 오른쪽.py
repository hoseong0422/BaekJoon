def solution(str_list):
    if str_list.count('l') == str_list.count('r') == 0:
        return []
    
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]
