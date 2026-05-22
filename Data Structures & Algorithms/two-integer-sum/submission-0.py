class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x=target-nums[i]
            for j in range(i+1,len(nums)):
                if x == nums[j]:
                    return [int(i),int(j)]
        