from collections import Counter
N = int(input())
common = Counter(input()).most_common(1)
print(*common[0], sep=' ')