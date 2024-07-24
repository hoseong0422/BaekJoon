import math

h, w, n, m = map(int, input().split())

max_rows = math.ceil(h / (1 + n))
max_cols = math.ceil(w / (1 + m))

answer = max_rows * max_cols
print(answer)