T = int(input())
for _ in range(T):
    idx, word = map(str, input().split())
    # temp = word[:]
    idx = int(idx)
    answer = word[:idx-1]+word[idx:]
    print(answer)