class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        eyes = {} 
        
        for i, num in enumerate(nums) :
            complement = target - num
            
            if complement in eyes  :
                return [eyes[complement], i]
            
            eyes[num] = i