def solution(clothes):
    clothes_dict = {}

    for c, t in clothes:
        if t not in clothes_dict:
            clothes_dict[t] = 2
        else:
            clothes_dict[t] += 1

    cnt = 1
    for num in clothes_dict.values():
        cnt *= num

    return cnt - 1