S = sum(list(map(int, input().split())))
T = sum(list(map(int, input().split())))
if S > T:
    print(S)
elif T > S:
    print(T)
elif T == S:
    print(S)