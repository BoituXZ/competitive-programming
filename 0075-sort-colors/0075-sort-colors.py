class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size):
            min = i
            for j in range(i + 1, size):
                if nums[j] < nums[min]:
                    min = j
            
            nums[i], nums[min] = nums[min], nums[i]
