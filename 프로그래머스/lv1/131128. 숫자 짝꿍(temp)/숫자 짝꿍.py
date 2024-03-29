def solution(X, Y):
    answer = ''

    temp = [i for i in X]
    for i in list(set(temp)):
        if X.count(i) > 0 and Y.count(i) > 0:
            if X.count(i) > Y.count(i):
                answer += i * Y.count(i)
            else:
                answer += i * X.count(i)

    answer_lst = [i for i in answer]
    answer_lst.sort(reverse=True)
    if len(answer_lst) != 0:
        return str(int(''.join(answer_lst)))
    else:
        return '-1'
    
# 풀리긴 하지만 시간초과 발생 나중에 해결해보기    