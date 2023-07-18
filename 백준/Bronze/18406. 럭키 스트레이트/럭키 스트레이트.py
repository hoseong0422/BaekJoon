data = input()

left = data[:len(data)//2]
right = data[len(data)//2:]
left_lst = [int(i) for i in left]
right_lst = [int(i) for i in right]

if sum(left_lst) == sum(right_lst):
    print('LUCKY')
else:
    print('READY')