def solution(my_string, queries):
    data = [i for i in my_string]
    for query in queries:
        a, b = query[0], query[1]
        data[a:b+1] = data[a:b+1][::-1]
    return ''.join(data)