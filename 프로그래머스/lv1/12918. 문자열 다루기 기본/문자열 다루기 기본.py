def solution(s):
    nums = [str(i) for i in range(10)]
    num_cnt = 0
    if len(s) != 4 and len(s) != 6:
        return False
    
    for l in s:
        if l not in nums:
            return False
        elif l in nums:
            num_cnt += 1
        
    if num_cnt == len(s):
        return True
    else:
        return False