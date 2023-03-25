N = int(input())
x_lst = []
y_lst = []
for _ in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
    
if N == 1:
    print(0)
else:
    x_len = max(x_lst) - min(x_lst)
    y_len = max(y_lst) - min(y_lst)
    print(x_len * y_len)