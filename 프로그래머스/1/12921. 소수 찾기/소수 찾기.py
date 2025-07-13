import math

def solution(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    prime = [2]
    limit = int(math.sqrt(n))

    # 홀수 리스트 작성
    data = [i + 1 for i in range(2, n, 2)]

    while limit >= data[0]:
        prime.append(data[0])
        # 나누어떨어지지 않은 수만 꺼냄
        data = [j for j in data if j % data[0] != 0]
    return len(prime + data)