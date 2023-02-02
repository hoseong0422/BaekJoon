nums = [0 for i in range(10)]
data = input()
for i in range(len(data)):
    num = int(data[i])
    if num == 6 or num == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[num] += 1
print(max(nums))