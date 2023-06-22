def solution(intStrs, k, s, l):
    answer = []
    for arr in intStrs:
        data = [i for i in arr]
        if int(''.join(data[s:l+s])) > k:
            answer.append(int(''.join(data[s:l+s])))
    return answer