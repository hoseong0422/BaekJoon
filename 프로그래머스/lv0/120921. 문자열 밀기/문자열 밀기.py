def solution(A, B):
    if A == B:
        return 0
    cnt = 0
    pushed_a = A
    for _ in range(len(A)):
        pushed_a = pushed_a[-1] + pushed_a[0:-1]
        cnt += 1
        if pushed_a == B:
            return cnt
    
    return -1