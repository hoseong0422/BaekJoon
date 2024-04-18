# 시간 단축 방법 좀더 고민해보기
from string import ascii_lowercase

lower_list = list(ascii_lowercase)

N = int(input())
data = input()

lower_dict = {}
for i in range(len(lower_list)):
    lower_dict[lower_list[i]] = i + 1

answer = 0

for i in range(N):
    answer += lower_dict[data[i]] * 31 ** i
print(answer)
