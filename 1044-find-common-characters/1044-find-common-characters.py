class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        min_character_frequencies = [0] * 26
        for character in words[0]:
            index = ord(character) - ord('a')
            min_character_frequencies[index] += 1
        
        for word_index in range(1, len(words)):
            current_word_frequencies = [0] * 26
            for character in words[word_index]:
                index = ord(character) - ord('a')
                current_word_frequencies[index] += 1
            
            for frequency_index in range(26):
                if current_word_frequencies[frequency_index] < min_character_frequencies[frequency_index]:
                    min_character_frequencies[frequency_index] = current_word_frequencies[frequency_index]
        
        common_characters_result = []
        for frequency_index in range(26):
            for count in range(min_character_frequencies[frequency_index]):
                character = chr(frequency_index + ord('a'))
                common_characters_result.append(character)
                
        return common_characters_result