N = int(input())
lst = list(map(int, input().split()))
if N/2 <= lst.count(0):
    print('INVALID')
else:
    if lst.count(1) > lst.count(-1):
        print('APPROVED')
    else:
        print('REJECTED')