agents = []
for i in range(1, 6):
    data = list(map(str, input().split('-')))
    for d in data:
        if 'FBI' in d:
            agents.append(i)
if len(agents) == 0:
    print('HE GOT AWAY!')
else:
    print(' '.join(str(s) for s in agents))