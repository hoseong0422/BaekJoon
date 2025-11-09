import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))          # 0=queue, 1=stack
B = list(map(int, input().split()))          # 초기 값들

# 큐(0)인 자료구조의 초기 값만, 주어진 순서대로 덱에 담기
D = deque(b for a, b in zip(A, B) if a == 0)

M = int(input().strip())
C = list(map(int, input().split()))          # 새로 들어올 값들

out = []
for x in C:
    D.appendleft(x)          # 새 값이 가장 왼쪽 큐로 들어감
    out.append(str(D.pop())) # 맨 오른쪽에서 하나 출력

print("".join(s + (" " if i < len(out)-1 else "") for i, s in enumerate(out)))
