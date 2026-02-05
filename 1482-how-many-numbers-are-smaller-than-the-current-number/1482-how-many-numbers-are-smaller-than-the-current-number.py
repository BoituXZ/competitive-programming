class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        

        dictionaryMap = {}
        for i, num in enumerate(sorted_nums):

            if num not in dictionaryMap:
                dictionaryMap[num] = i
        

        output = []
        for num in nums:
            output.append(dictionaryMap[num])
            
        return output