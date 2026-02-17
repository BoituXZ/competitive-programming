class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = "".join(char.lower() for char in s if char.isalnum())
    
        return final_string == final_string[::-1]