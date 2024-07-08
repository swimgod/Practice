from typing import List


class WordPattern:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        split_words = s.split(' ')
        word_dict = {}
        word_set = set()

        if len(split_words) != len(pattern):
            return False
        for i in range(len(pattern)):
            char_pattern = pattern[i]
            word = split_words[i]
            if char_pattern not in word_dict:
                if word in word_set:
                    return False
                word_dict[char_pattern] = word
                word_set.add(word)
            else:
                if word_dict[char_pattern] != word:
                    return False
        return True
