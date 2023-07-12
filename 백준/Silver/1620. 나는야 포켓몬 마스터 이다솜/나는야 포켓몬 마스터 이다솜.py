import sys

input = sys.stdin.readline
N, M = map(int, input().split())

cnt = 1
poke_dict = {}
for _ in range(N):
    a = input().rstrip()
    poke_dict[a] = cnt
    poke_dict[cnt] = a
    cnt += 1

for _ in range(M):
    b = input().rstrip()
    if b.isdigit() == True:
        print(poke_dict[int(b)])
    else:
        print(poke_dict[b])