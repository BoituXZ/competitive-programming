class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        targets = set(range(left, right + 1))
        

        covered_set = {num for start, end in ranges for num in range(start, end + 1)}
        
        return targets.issubset(covered_set)