data = input()

k_count = 0
y_count = 0
printed = False

k_dict = {}
y_dict = {}
for k in 'KOREA':
    k_dict[k] = 0
for y in 'YONSEI':
    y_dict[y] = 0    
  
if 'K' not in data or 'R' not in data or 'A' not in data:
    print('YONSEI')
    printed = True
elif 'Y' not in data or 'N' not in data or 'S' not in data or 'I' not in data:
    print('KOREA')
    printed = True
    
for i in data:
    if printed == True:
        break
    
    if i in 'KOREA' and i in 'YONSEI':
        if k_dict[i] == 0:
            k_dict[i] = 1
            k_count += 1
        if y_dict[i] == 0:
            y_dict[i] = 1
            y_count += 1
    elif i in 'KOREA' and i not in 'YONSEI':
        if k_dict[i] == 0:
            k_dict[i] = 1
            k_count += 1
    else:
        if y_dict[i] == 0:
            y_dict[i] = 1
            y_count += 1
    
    if k_count == 5:
        print('KOREA')
        break
    if y_count == 6:
        print('YONSEI')
        break