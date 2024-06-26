class RansomNote:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        unique_letters = list(set(magazine))
        magazine_letter_pool = {letter: magazine.count(letter) for letter in unique_letters}

        for letter in ransomNote:
            if letter in magazine_letter_pool and magazine_letter_pool[letter] != 0:
                magazine_letter_pool[letter] -= 1
            else:
                return False
        return True
