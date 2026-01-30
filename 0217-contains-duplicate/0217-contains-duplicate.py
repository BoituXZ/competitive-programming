class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

        if len(set(nums)) == len(nums) or len(nums) == 0:
            return False
        else:
            return True

        