data = input()
len_data = len(data)
j_cnt = 0
i_cnt = 0

for i in range(len_data - 2):
    if data[i:i+3] == 'JOI':
        j_cnt += 1
    elif data[i:i+3] == 'IOI':
        i_cnt += 1

print(j_cnt, i_cnt, sep='\n')