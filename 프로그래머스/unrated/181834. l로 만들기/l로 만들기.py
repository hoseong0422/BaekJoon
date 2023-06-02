import string

def solution(myString):
    alphabet = list(string.ascii_lowercase)
    target = alphabet[:alphabet.index('l')]
    answer = ''
    
    for i in myString:
        if i in target:
            answer += 'l'
        else:
            answer += i
    return answer