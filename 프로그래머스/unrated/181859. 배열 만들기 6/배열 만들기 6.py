from collections import deque

def solution(arr):
    answer = deque([])
    i = 0
    while len(arr) > i:
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        else:
            if arr[i] == answer[-1]:
                answer.pop()
                i += 1
            else:
                answer.append(arr[i])
                i += 1
    if len(answer) == 0:
        answer.append(-1)
    return list(answer)