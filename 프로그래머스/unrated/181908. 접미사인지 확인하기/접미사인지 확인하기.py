def solution(my_string, is_suffix):
    end = len(is_suffix)
    if my_string[-end:] == is_suffix:
        return 1
    else:
        return 0