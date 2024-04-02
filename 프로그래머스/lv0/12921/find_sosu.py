# 시간초과 다시 풀어보기

def solution(n):
    answer = 0

    for i in range(2, n+1):
        temp = 0
        for j in range(2, i + 1):
            if i % j == 0:
                temp += 1
        if temp == 1:
            answer += 1
    
    return answer
