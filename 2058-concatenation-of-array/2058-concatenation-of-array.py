class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        original = len(nums)
        
        result = [0] * (2 * original)
        
        for i in range(original):
            result[i] = nums[i]
            
            result[i + original] = nums[i]
            
        return result