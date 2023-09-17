alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
S = input()
cnt = 1
for i in range(len(S) - 1):
    if alpha.index(S[i]) >= alpha.index(S[i + 1]):
        cnt += 1
print(cnt)