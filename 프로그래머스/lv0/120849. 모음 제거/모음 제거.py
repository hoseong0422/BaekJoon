def solution(my_string):
    vowels = ['a', 'e', 'o', 'u', 'i']
    answer = ''
    for i in my_string:
        if i not in vowels:
            answer += i
    return answer