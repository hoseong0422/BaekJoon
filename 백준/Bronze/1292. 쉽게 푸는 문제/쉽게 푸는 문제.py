A, B = map(int, input().split())
nums = []
for i in range(B):
    for j in range(i+1):
        nums.append(i+1)
print(sum(nums[A-1:B]))