class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(len(nums)):
                    if i == j:
                        continue
                    elif nums[i]+ nums[j] == target:
                        return [i, j]
                    else:
                        continue
                        

