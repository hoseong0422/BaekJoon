from string import ascii_lowercase

lower_list = list(ascii_lowercase)

N = int(input())
data = input()

answer = 0

for i in range(N):
    answer += (lower_list.index(data[i]) + 1) * 31 ** i
print(answer)