class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 # left pointer
        right = len(height) - 1 # right pointer

        left_max = 0 # tallest wall from the left
        right_max = 0 # tallest wall from the right
        water = 0 # result

        while left < right:
            left_max = max(left_max, height[left]) # updating the max left in each iteration
            right_max = max(right_max, height[right]) # updating the max right in each iteration 

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
