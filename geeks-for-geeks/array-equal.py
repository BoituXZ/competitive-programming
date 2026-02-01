class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        

        if len(a) != len(b):
            return False
            
        return a == b
