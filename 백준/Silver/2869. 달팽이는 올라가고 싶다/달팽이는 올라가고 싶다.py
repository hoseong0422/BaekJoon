import math
A, B, V = map(int, input().split(" "))
cnt = (V - B) / (A - B)
# 올림을 사용하여 딱 떨어지지 않을 때 하루 더 추가 되도록 함
print(math.ceil(cnt))