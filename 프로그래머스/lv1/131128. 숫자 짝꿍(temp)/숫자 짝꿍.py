from itertools import combinations

def solution(number):
    answer = 0
    combination = list(combinations(number, 3))
    for combi in combination:
        if sum(combi) == 0:
            answer += 1
    return answer