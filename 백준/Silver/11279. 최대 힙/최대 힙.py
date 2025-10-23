import sys
import heapq

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    heap = []  # 여기에 -x로 저장 (min-heap을 max-heap처럼 사용)
    out = []

    for _ in range(n):
        x = int(input().strip())
        if x == 0:
            if heap:
                out.append(str(-heapq.heappop(heap)))  # 부호 되돌려서 출력
            else:
                out.append('0')
        else:
            heapq.heappush(heap, -x)  # 음수로 넣기

    print('\n'.join(out))

if __name__ == "__main__":
    solve()
