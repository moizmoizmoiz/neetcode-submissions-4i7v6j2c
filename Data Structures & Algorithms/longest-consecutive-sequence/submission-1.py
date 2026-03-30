class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        long = 0
        numset = set(nums)
        
        for num in numset:

            if num - 1 not in numset:
                leng =  1
                while num + leng in numset:
                    leng += 1
                long = max(leng , long)



        return long