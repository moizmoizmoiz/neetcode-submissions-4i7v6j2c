class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i, x in enumerate(nums):
            copy = nums.copy()
            copy.pop(i)

            print(f"nums = {nums}, copy = {copy}")
            
            ans = 1
            

            for j in range(len(copy)):
                ans = ans * copy[j]
           
            result.append(ans)


        return result