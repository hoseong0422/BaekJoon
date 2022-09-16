import sys
odd_list = []
for _ in range(7):
    num = int(sys.stdin.readline().rstrip())
    if num % 2 != 0:
        odd_list.append(num)
if len(odd_list) > 0:
    print(sum(odd_list))
    odd_list.sort()
    print(odd_list[0])
else:
    print(-1)