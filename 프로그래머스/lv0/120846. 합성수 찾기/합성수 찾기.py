def solution(n):
    answer = 0
    for i in range(1, n+1):
        factors = []
        for j in range(1, i+1):
            if i % j ==0:
                factors.append(j)
        if len(factors) >= 3:
            answer += 1
    return answer