def solution(s):
    data = [i for i in s]
    data.sort(reverse=True)
    return ''.join(data)