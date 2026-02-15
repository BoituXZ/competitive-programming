class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        permutation_result = []
        
        for index in range(len(nums)):
            target = nums[nums[index]]
            permutation_result.append(target)
            
        return permutation_result