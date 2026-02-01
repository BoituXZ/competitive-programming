class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
    
        strs.sort()
        
        firstCharacter = strs[0]
        lastCharacter = strs[-1]
        longestPrefix = []
        
        for i in range(min(len(firstCharacter), len(lastCharacter))):
            if firstCharacter[i] == lastCharacter[i]:
                longestPrefix.append(firstCharacter[i])
            else:
                break
                
        return "".join(longestPrefix)
