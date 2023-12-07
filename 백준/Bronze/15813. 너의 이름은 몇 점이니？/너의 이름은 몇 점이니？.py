import string

alpha_lst = list(string.ascii_uppercase)
alpha_dict = {}

i = 1
for alpha in alpha_lst:
    alpha_dict[alpha] = i
    i += 1

N = int(input())
name = input()

point = 0
for n in name:
    point += alpha_dict[n]

print(point)