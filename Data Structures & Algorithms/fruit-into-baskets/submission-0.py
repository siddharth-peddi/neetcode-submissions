class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = {}
        longest = 0

        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            w = r - left + 1
            longest = max(longest, w)
        
        return longest