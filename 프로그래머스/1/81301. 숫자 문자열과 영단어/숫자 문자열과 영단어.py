def solution(s):
    number_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'}
    answer = ''
    temp = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in number_dict.keys():
                answer += number_dict[temp]
                temp = '' 
    return int(answer)