N = int(input())

row = 1
while N > row:
    N -= row
    row += 1

if row % 2 == 0: # 짝수일때
    a = N
    b = row - N + 1
else:
    a = row - N + 1
    b = N
print(a, '/', b, sep="")