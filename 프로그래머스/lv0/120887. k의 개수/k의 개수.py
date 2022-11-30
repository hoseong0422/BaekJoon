def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        if len(str(n)) == 1:
            if str(k) in str(n):
                answer += 1
        else:    
            for j in str(n):
                if str(k) in str(j):
                    answer += 1
    return answer