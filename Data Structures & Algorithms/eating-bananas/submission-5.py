class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:    
        ## piles = [1,4,3,2], h = 9  
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
        
            if hours <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer