class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = nums.count(0)
        if len(nums) == zero_cnt:
            nums = nums
        else:
            nums[:] = [i for i in nums if i != 0]
            nums += [0 for _ in range(zero_cnt)]