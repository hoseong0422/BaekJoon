def solution(lines):
    cnt = [0 for _ in range(200)]
    answer = 0
    for line in lines:
        for i in range(line[0], line[1]):
            cnt[i + 100] += 1
    answer += cnt.count(2)
    answer += cnt.count(3)
    return answer