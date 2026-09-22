class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[r])

            w = r - left + 1
            longest = max(longest, w)

        return longest