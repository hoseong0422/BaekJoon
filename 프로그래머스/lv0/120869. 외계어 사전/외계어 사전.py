def solution(spell, dic):
    answer = 0
    
    for word in dic:
        splited_word = [i for i in word]
        cnt = 0
        for s in spell:
            if s in splited_word:
                cnt += 1
        if cnt >= len(spell):
            answer += 1
    if answer >= 1:
        return 1
    else:
        return 2