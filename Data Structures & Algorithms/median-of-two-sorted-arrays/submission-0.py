class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # BRUTE FORCE METHOD - O(m + n)
        
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        print(nums3)

        if n % 2 == 1: #odd
            median = n // 2
            return nums3[median]
        else:
            median = (n - 1) // 2
            median2 = ((n - 1) // 2) + 1

            print(median, median2, nums3[median], nums3[median2] )

            return (nums3[median] + nums3[median2]) / 2

