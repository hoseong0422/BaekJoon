A, B, C = map(int, input().split())

# 생산 비용이 판매가격보다 크거나 같다면 손익분기점이 존재하지 않는다.
if B >= C:
    print(-1)
# C * x = A + (B * x) -> x = A / (C-B)
# 손익 분기점을 정리하면 A / (C - B)가 되고 이익을 발생하는 시점을 + 1부터로 정의
else:
    print(int(A/(C-B)+1))