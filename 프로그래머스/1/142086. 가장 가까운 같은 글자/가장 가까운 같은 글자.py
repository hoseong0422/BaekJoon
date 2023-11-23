def solution(s):
    pos_dict = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in pos_dict.keys():
            answer.append(-1)
            pos_dict[s[i]] = i
        else:
            answer.append(i - pos_dict[s[i]])
            pos_dict[s[i]] = i
    
    return answer