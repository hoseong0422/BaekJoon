def solution(myString, pat):
    answer = 0
    str_len = len(myString)
    for i in range(str_len - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer