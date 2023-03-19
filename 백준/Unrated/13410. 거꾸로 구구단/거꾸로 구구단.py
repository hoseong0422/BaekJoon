N, K = map(int, input().split())
lst = [int(str(i * N)[::-1]) for i in range(1, K+1)]
print(max(lst))