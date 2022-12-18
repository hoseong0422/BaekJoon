from collections import Counter
def solution(array):
    data = Counter(array).most_common(2)
    print(data)
    if len(array) == 1 or len(list(set(array))) == 1:
        return array[0]
    else:
        if data[0][1] != data[1][1]:
            return data[0][0]
        else:
            return -1