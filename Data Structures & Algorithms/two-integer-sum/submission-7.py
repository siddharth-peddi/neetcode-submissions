class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we're given an array of numbers
        # we have to find which two numbers = target
        # and return those indices

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return[seen[complement], i]
            seen[num] = i