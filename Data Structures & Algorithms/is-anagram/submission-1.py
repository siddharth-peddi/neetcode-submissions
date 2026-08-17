class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            counts[char] = counts.get(char, 0) - 1
        for count in counts.values():
            if count != 0:
                return False

        return True