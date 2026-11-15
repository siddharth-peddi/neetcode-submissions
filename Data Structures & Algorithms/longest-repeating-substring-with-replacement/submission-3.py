class Solution:
    def characterReplacement(self, s, k):
        left = 0
        longest = 0 
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_values = max(count.values())

            window = right - left + 1
            replacements = window - max_values

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                max_values = max(count.values())

                window = right - left + 1
                replacements = window - max_values

            longest = max(longest, window)
        
        return longest