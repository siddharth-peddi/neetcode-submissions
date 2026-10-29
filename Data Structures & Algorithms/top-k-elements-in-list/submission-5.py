class Solution:
    def topKFrequent(self, nums, k):
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        entries = sorted(
            counts.items(),
            key = lambda x : x[1],
            reverse = True
        )

        return [num for num, c in entries[:k]]