N = int(input())
for _ in range(N):
    data = input()
    if 'Simon says' in data:
        print(data[10:])