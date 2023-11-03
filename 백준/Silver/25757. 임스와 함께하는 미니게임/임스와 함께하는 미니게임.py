N, G = map(str, input().split())
N = int(N)

members = []
for _ in range(N):
    member = input()
    members.append(member)

members = set(members)

if G == 'Y':
    print(len(members))
elif G == 'F':
    print(len(members) // 2)
elif G == 'O':
    print(len(members) // 3)