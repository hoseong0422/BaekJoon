while True:
    N = int(input())
    if N == 0:
        break
    names = []
    heights = []
    for _ in range(N):
        n, h = map(str, input().split())
        names.append(n)
        heights.append(float(h))
    max_h = max(heights)
    answer = []
    for i in range(len(heights)):
        if heights[i] == max_h:
            answer.append(names[i])
    print(*answer, sep=' ')