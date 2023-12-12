N = int(input())
S = [input() for _ in range(N)]

M = int(input())
A = [input() for _ in range(M)]

loc = S.index('?')

for a in A:
    if N == 1:
        answer = A[0]
    elif loc == 0:
        if a not in S and S[loc + 1][0] == a[-1]: # ? 가 제일 앞이면 S[1] 문자의 제일 앞글자와 a의 제일 뒷글자가 같으면 된다
            answer = a
            break
    elif loc == N - 1:
        if a not in S and S[loc - 1][-1] == a[0]: # ? 가 제일 뒤면 S[-2] 문자의 제일 뒷글자와 a의 제일 앞글자가 같으면 된다
            answer = a
            break
    else:
        if a not in S and S[loc-1][-1] == a[0] and S[loc + 1][0] == a[-1]:
            answer = a
            break

print(answer)