# description : https://leetcode.com/problems/sum-of-unique-elements/description/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_dict = {}
        answer = 0
        
        for n in nums:
            if n not in nums_dict.keys():
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1
        
        for key in nums_dict:
            if nums_dict[key] == 1:
                answer += key
        
        return answer
