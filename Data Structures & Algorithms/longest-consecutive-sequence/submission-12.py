class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 0

                while current in num_set:
                    length += 1
                    current += 1

                longest = max(longest, length)

        return longest