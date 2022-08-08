total = int(input())
N = int(input())

bill = 0

for i in range(N):
    product, num = map(int, input().split())
    bill += (product * num)
if bill == total:
    print("Yes")
else:
    print("No")