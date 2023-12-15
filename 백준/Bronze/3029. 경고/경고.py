init = list(map(int, input().split(':')))
target = list(map(int, input().split(':')))

if init[2] > target[2]:
    S = 60 - init[2] + target[2]
    init[1] += 1
else:
    S = target[2] - init[2]

if init[1] > target[1]:
    M = 60 - init[1] + target[1]
    init[0] += 1
else: M = target[1] - init[1]

if init[0] > target[0]:
    H = 24 - init[0] + target[0]
else: H = target[0] - init[0]

if init[0] == target[0] and init[1] == target[1] and init[2] == target[2]:
    H = 24
    M = 0
    S = 0

if len(str(S)) == 1:
    S = f'0{S}'
if len(str(M)) == 1:
    M = f'0{M}'
if len(str(H)) == 1:
    H = f'0{H}'

print(f'{H}:{M}:{S}')