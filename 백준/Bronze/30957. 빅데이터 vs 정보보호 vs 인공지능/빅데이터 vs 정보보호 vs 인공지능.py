N = int(input())

data = input()

b_cnt = data.count('B')
s_cnt = data.count('S')
a_cnt = data.count('A')

if b_cnt == s_cnt == a_cnt:
    print('SCU')
elif b_cnt > s_cnt and b_cnt > a_cnt:
    print('B')
elif s_cnt > b_cnt and s_cnt > a_cnt:
    print('S')
elif a_cnt > s_cnt and a_cnt > b_cnt:
    print('A')
elif a_cnt == s_cnt and a_cnt > b_cnt:
    print('SA')
elif a_cnt == b_cnt and a_cnt > s_cnt:
    print('BA')
elif s_cnt == b_cnt and b_cnt > a_cnt:
    print('BS')