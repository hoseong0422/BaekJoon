import sys
input = sys.stdin.readline

staff = set()
N = int(sys.stdin.readline())
for _ in range(N):
    name, log = map(str, sys.stdin.readline().split())
    if log == 'enter':
        staff.add(name)
    elif log == 'leave':
        staff.remove(name)
answer = sorted(staff, reverse=True)
print(*answer, sep='\n')