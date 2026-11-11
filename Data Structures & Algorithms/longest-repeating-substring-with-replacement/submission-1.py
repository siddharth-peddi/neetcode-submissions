class Solution:
    def characterReplacement(self, s, k):
        left = 0 # the substring starts here
        count = {} # keeping a count of the characters
        longest = 0 # longest substring we've found

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(count.values())

            window_length = right - left + 1
            replacements = window_length - max_frequency

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                max_frequency = max(count.values())
                replacements = window_length - max_frequency

            longest = max(longest, window_length)
        return longest