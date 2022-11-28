from itertools import permutations

def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    cnt = 0
    word = []
    for i in range(1, len(possible)+1):
        for j in permutations(possible, i):
            word.append(''.join(j))
    
    for i in babbling:
        if i in word:
            cnt += 1
    return cnt