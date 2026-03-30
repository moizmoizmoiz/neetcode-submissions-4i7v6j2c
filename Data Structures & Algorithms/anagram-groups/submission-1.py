class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dick = defaultdict(list)
        result = []

        for i,x in enumerate(strs):
            sub = "".join(sorted(x))

            (dick[sub]).append(x)

        print(dick)

        # for x in dick:
        #     group = []
        #     for y in dick[x]:
        #         group.append(strs[y])
            
        #     result.append(group)


        # return result

        return list(dick.values())