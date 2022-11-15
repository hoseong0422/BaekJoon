import string
def solution(age):
    alpha = list(string.ascii_lowercase)
    answer = ''
    for i in str(age):
        answer += alpha[int(i)]
    return answer