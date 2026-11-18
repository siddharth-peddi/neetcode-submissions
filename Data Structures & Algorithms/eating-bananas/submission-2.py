class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:    
        ## piles = [1,4,3,2], h = 9  
        left = 1
        right = max(piles) # this case 4
        answer = right

        while left <= right:
            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                answer = mid # save it
                right = mid - 1 # searching for a lower speed
            else:
                left = mid + 1
        return answer