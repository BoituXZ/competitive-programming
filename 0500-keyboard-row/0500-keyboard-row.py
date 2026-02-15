class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row_top = set("qwertyuiop")
        row_middle = set("asdfghjkl")
        row_bottom = set("zxcvbnm")
        
        valid_words = []
        
        for word in words:
            word_set = set(word.lower())

            if word_set.issubset(row_top) or \
               word_set.issubset(row_middle) or \
               word_set.issubset(row_bottom):
                valid_words.append(word)
                
        return valid_words