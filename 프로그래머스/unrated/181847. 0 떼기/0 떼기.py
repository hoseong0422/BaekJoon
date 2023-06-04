def solution(n_str):
    answer = ''
    lst_str = [i for i in n_str]
    for i in range(len(lst_str)):
        if lst_str[0] != '0':
            return n_str
        else:
            if i == 0:
                continue
            elif lst_str[i - 1] != lst_str[i]:
                return ''.join(lst_str[i:])