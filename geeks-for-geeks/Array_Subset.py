#User function Template for python3


class Solution:
    def isSubset(self, a, b):
     
        frequency = {}
        
    
        for num in a:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
    
        for num in b:
          
            if num not in frequency or frequency[num] == 0:
                return False
            
         
            frequency[num] -= 1
            
        return True
