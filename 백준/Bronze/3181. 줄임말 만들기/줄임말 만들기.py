skip_str = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
data = input()
answer = ''
split_data = data.split()
for i in range(len(split_data)):
    if i == 0 or split_data[i] not in skip_str:
        answer += split_data[i][0].upper()
print(answer)