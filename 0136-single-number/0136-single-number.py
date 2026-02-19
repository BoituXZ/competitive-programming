class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_result = 0
        
        for current_num in nums:
            unique_result ^= current_num
            
        return unique_result