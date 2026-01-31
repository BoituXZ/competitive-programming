class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = None
        counter = 0
        
        for number in nums:

            if counter == 0:
                element = number

            if number == element:
                counter += 1
            else:
                counter -= 1
                
        return element