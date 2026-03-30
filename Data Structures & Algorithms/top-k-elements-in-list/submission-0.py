class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(list)
        result = []


        for x in nums:
            
            bucket[x] = bucket.get(x, 0) + 1

        print(bucket)
        print(max(bucket))
        print(max(bucket, key = bucket.get))


        for i in range(k):
            
            key = max(bucket, key = bucket.get)
            result.append(key)

            del bucket[key]

        return result
        