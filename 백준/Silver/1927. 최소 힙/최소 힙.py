import sys
import heapq

input = sys.stdin.readline  # 빠른 입력

N = int(input())
heap = []
result = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            result.append(str(heapq.heappop(heap)))
        else:
            result.append('0')
    else:
        heapq.heappush(heap, x)

# 빠른 출력
print('\n'.join(result))
