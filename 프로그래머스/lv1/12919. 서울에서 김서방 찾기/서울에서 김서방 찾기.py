def solution(seoul):
    cnt = 0
    for i in seoul:
        if i == 'Kim':
            answer = f'김서방은 {cnt}에 있다'
            return answer
        cnt += 1