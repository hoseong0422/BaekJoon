N = int(input())
data = input()

if data.count('bigdata') > data.count('security'):
    print('bigdata?')
elif data.count('bigdata') < data.count('security'):
    print('security!')
else:
    print('bigdata? security!')