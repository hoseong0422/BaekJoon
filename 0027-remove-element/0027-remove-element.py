class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        for _ in range(cnt):
            nums.remove(val)
        answer = len(nums)
        answer_lst = nums + ['_' for i in range(cnt)]
        return print(f"{answer}, nums = {answer_lst}")