from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = Counter(magazine)
        note_letters = Counter(ransomNote)

        for letter, count in note_letters.items():
            if letter not in magazine_letters:
                return False

            if note_letters[letter] > magazine_letters[letter]:
                return False

        return True
