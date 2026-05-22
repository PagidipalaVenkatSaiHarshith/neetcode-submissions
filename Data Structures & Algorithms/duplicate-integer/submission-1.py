class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for i in nums:
            dup[i]=0
        for i in nums:
            dup[i] += 1
        for i in dup.values():
            if i>1:
                return True
        return False