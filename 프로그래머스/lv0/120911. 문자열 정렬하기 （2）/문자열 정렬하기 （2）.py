def solution(my_string):
    data = ""
    for i in my_string:
        if i.lower() != i:
            data += i.lower()
        else:
            data += i
    answer = sorted(data)
    return ''.join(answer)