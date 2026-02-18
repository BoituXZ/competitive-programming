class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffled_list = [''] * len(s)
        
        for i in range(len(s)):
            shuffled_list[indices[i]] = s[i]
            
        final_result = "".join(shuffled_list)
        return final_result