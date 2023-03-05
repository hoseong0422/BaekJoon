from collections import deque
data = []
for _ in range(5):
    queue = deque([i for i in input()])
    data.append(queue)

answer = ''
max_len = 0
for d in data:
    if len(d) > max_len:
        max_len = len(d)
for _ in range(max_len):
    for dq in data:
        if len(dq) > 0:
            answer += dq.popleft()
print(answer)