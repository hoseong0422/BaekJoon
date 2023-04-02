from collections import Counter
import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(N)]

numbers = sorted(numbers)
cnt = Counter(numbers).most_common()
# 산술평균
print(round(sum(numbers) / len(numbers)))
# 중앙값
print(numbers[N//2])
# 최빈값
if len(numbers) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
# 범위
print(max(numbers) - min(numbers))