matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))
max_num = -1
row_cnt = 0

for row in matrix:
    row_cnt += 1
    if max(row) > max_num:
        max_num = max(row)
        max_idx = row.index(max_num)
        max_row = row_cnt

print(max_num)
print(f'{max_row} {max_idx + 1}')