def solution(a, b, c, d):
    data = [a, b, c, d]
    if len(set(data)) == 1:
        return a * 1111
    elif len(set(data)) == 4:
        return min(data)
    elif len(set(data)) == 2:
        cnt = 0
        for i in data:
            if cnt < data.count(i):
                cnt = data.count(i)
        if cnt == 2:
            temp = list(set(data))
            if temp[0] - temp[1] < 0:
                return (temp[0] + temp[1]) * ((temp[0] - temp[1]) * -1)
            else:
                return (temp[0] + temp[1]) * (temp[0] - temp[1])
        elif cnt == 3:
            data.sort()
            if data[0] != data[1]:
                return ((10 * data[1]) + data[0]) ** 2
            else:
                return ((10 * data[2]) + data[3]) ** 2
    else:
        temp = []
        for i in data:
            if data.count(i) != 2:
                temp.append(i)
        return temp[0] * temp[1]
        
                