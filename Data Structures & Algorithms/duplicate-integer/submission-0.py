class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size_of_list = len(nums)
        size_of_set = len(set(nums))

        if size_of_list > size_of_set:
            return True
        else:
            return False