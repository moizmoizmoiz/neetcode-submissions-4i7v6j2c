class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxy = 0
    
        # for left in range(len(heights)):
        #     for right in range(len(heights) -1, 0, -1):
                # while left < right:

        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                    area = min(heights[left], heights[right]) * (right - left)
                    # right -= 1
                    maxy = max(maxy, area)
                # continue

        return maxy