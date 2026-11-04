class Solution:
    def maxArea(self, heights):
        left = 0 # the pointer on the left
        right = len(heights) - 1 # the pointer on the right
        max_area = 0 # this holds the max area

        while left < right:
            width = right - left # this will give the width
            height = min(heights[left], heights[right]) # we need the smaller of the two bc anything above that will overflow and not contain the water
            area = width * height # formula

            max_area = max(area, max_area) # we want the max area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

