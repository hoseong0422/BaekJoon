N = int(input())
for _ in range(N):
    s = input()
    if s[-1] == '.':
        print(s)
    else:
        print(f'{s}.')