def solution(clothes):
    cloth_dict = {k:[] for _,k in clothes}
    for v, k in clothes:
        cloth_dict[k].append(v)
    res = 1
    for v in cloth_dict.values():
        res *= (len(v) + 1)
    return res - 1
