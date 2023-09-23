N = int(input())
for _ in range(N):
    data = str(input())
    
    if data[ len(data) // 2 - 1 ] == data[ len(data) // 2 ]:
        print('Do-it')
    else:
        print('Do-it-Not')