# nums is the given input
# return true if there are two or more of the same number
# or return false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums: 
            if num in seen:
                return True
            seen.add(num)
        
        return False