from string import ascii_lowercase, ascii_uppercase

def solution(my_string):
    lowercase_list = list(ascii_lowercase)
    uppercase_list = list(ascii_uppercase)

    total_alphabet = uppercase_list + lowercase_list
    
    lst_string = [i for i in my_string]
    
    answer = [0 for i in range(len(total_alphabet))]
    for i in range(len(total_alphabet)):
        if lst_string.count(total_alphabet[i]) > 0:
            answer[i] = lst_string.count(total_alphabet[i])
    return answer