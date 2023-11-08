import string
upper_alpha = list(string.ascii_uppercase)

alpha_dict = {}
for i, alpha in zip(range(65, 91), upper_alpha):
    alpha_dict[alpha] = i

N = int(input())

for _ in range(N):
    alpha_sum = sum([i for i in range(65, 91)])
    data = input()

    data = list(set([i for i in data]))
    
    for j in data:
        alpha_sum -= alpha_dict[j]
    print(alpha_sum)