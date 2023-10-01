data = input()
h_count = data.count(':-)')
s_count = data.count(':-(')

if h_count > s_count:
    print('happy')
elif s_count > h_count:
    print('sad')
elif h_count == 0 and s_count == 0:
    print('none')    
elif h_count == s_count:
    print('unsure')