N = int(input())

S = ['Never gonna give you up', 
     'Never gonna let you down',
     'Never gonna run around and desert you',
     'Never gonna make you cry',
     'Never gonna say goodbye',
     'Never gonna tell a lie and hurt you',
     'Never gonna stop']
cnt = 0

for _ in range(N):
    data = input()

    if data not in S:
        print('Yes')
        break
    else:
        cnt += 1
if cnt == N:
    print('No')