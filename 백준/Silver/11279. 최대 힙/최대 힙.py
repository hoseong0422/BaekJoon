import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())

max_heap = [] # 여기에 -x로 저장 (min-heap을 max-heap처럼 사용)
result = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if max_heap:
            result.append(str(-heapq.heappop(max_heap))) # 부호 되돌려서 출력
        else:
            result.append('0')
    else:
        heapq.heappush(max_heap, -x) # 음수로 넣기
    
print('\n'.join(result))

