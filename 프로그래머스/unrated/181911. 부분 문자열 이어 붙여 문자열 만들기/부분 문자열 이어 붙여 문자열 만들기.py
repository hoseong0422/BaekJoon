def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer += my_strings[i][int(parts[i][0]):int(parts[i][1]+1)]
    return answer