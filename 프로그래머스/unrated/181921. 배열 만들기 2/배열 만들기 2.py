def solution(l, r):
    result = []

    for i in range(l, r+1):
        if i % 5 != 0:
            continue

        data = str(i) 
        temp = True

        for j in data:
            if j != "5" and j != "0":            
                temp = False
        if temp == True:
            result.append(i)

    if len(result) == 0:
        return [-1]
    return result