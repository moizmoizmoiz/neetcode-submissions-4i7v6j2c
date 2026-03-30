class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for n in range(len(numbers)):
            diff = target - numbers[n]

            if hashmap[diff]:
                return [hashmap[diff], n+1]
            
            hashmap[numbers[n]] = n+1

        return []