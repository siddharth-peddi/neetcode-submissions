class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        entries = sorted(
            count.items(),
            key = lambda x: x[1],
            reverse = True
        )

        topK = entries[:k]
        
        return [entry[0] for entry in topK]