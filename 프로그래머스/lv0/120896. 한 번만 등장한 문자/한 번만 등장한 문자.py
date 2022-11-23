def solution(s):
    init = []
    removed = []
    for i in s:
        if i in removed:
            continue
        elif i not in init:
            init.append(i)
        elif i in init:
            init.remove(i)
            removed.append(i)
    init.sort()
    return ''.join(init)