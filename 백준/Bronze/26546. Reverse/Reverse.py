N = int(input())

for _ in range(N):
    word, i, j = map(str, input().split())

    answer = ''
    
    for k in range(len(word)):
        if k < int(i) or k >= int(j):
            answer += word[k]
    print(answer)