class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_alphabet = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        unique_transformations = set()
        
        for word in words:
            current_word_transformation = []
            
            for char in word:
                char_index = ord(char) - ord('a')
                current_word_transformation.append(morse_alphabet[char_index])
            
            full_morse_string = "".join(current_word_transformation)
            unique_transformations.add(full_morse_string)
            
        return len(unique_transformations)