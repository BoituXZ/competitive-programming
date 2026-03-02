class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        for index, number in enumerate(nums):
            if number == target:
                indices.append(index)
        return indices