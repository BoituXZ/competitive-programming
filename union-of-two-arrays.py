class Solution:    
    def findUnion(self, a, b):
        s1 = set(a)
        s2 = set(b)
        
        return s1 | s2
