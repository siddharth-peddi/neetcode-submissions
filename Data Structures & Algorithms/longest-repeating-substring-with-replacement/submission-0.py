class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest = 0
        max_frequency = 0 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_frequency = max(max_frequency, count[s[r]])

            while (r - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, r - left + 1)
        return longest