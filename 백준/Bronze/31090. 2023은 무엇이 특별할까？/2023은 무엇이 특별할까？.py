N = int(input())

for _ in range(N):
    data = str(input())

    if (int(data) + 1) % int(data[-2:]) == 0:
        print('Good')
    else:
        print('Bye')