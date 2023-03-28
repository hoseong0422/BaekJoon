def solution(score):
    answer = []
    avg = []
    for s in score:
        avg.append(sum(s) / len(s))
        
    sorted_lst = sorted(avg, reverse=True)
    
    for i in avg:
        answer.append(sorted_lst.index(i)+1)
    return answer