class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(f"number:\n{nums}")
        
        size = len(nums)
        result = [0] * size
        pref = [0] * size
        suff = [0] * size
        
        pref[0] = suff[size - 1] = 1
        
        print("\nBefore")
        print(pref)
        print(suff)
        

        for i in range(1, size):
            pref[i] = nums[i-1] * pref[i - 1]

        for i in range(size-2, -1, -1):
            # remember this starts from revers aka 13..12..11..10 etc.
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(size):
            result[i] = suff[i] * pref[i]

        print("\n\n After")
        print(pref)
        print(suff)
        print(result)
        

        return result


