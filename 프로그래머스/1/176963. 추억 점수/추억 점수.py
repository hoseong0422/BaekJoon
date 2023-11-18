def solution(name, yearning, photo):
    answer = []
    point_dict = {}

    for n, y in zip(name, yearning):
        point_dict[n] = y
        
    for pho in photo:
        temp = 0
        for p in pho:
            if p in point_dict.keys():
                temp += point_dict[p]
        answer.append(temp)
    return answer