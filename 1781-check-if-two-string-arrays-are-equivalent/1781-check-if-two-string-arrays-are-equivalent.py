class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        full_string_one = "".join(word1)
        full_string_two = "".join(word2)
        

        return full_string_one == full_string_two