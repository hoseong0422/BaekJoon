punch = input()
left = punch.split('(^0^)')[0].count('@')
right = punch.split('(^0^)')[-1].count('@')
print(f'{left} {right}')