class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_sum = 0
        for i in t:
            hash_sum += hash(i)
        
        for j in s:
            hash_sum -= hash(j)
        
        if hash_sum == 0:
            return True
        else:
            return False