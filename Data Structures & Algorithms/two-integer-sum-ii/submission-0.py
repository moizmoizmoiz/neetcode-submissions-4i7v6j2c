class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, inum in enumerate(numbers):
            for j, jnum in enumerate(numbers):
                if i == j:
                    continue
                
                if inum + jnum == target:
                    return [i+1, j+1]