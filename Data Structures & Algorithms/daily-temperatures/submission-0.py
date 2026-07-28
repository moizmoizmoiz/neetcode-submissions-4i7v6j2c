class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # VERY VERY NAIVE DUMBASS 2 POINTER STYLE SOLUTION WITH O(n^2)
        result = []

        for i in range(len(temperatures)):
            print("i",  i, temperatures[i])
            count = 0
            for j in range(i+1, len(temperatures)):
                print("j",  j, temperatures[j])
                if temperatures[i] < temperatures[j]:
                    count += 1
                    result.append(count)
                    print(count)
                    break
                elif j == len(temperatures)-1:
                    result.append(0)
                else:
                    count += 1
                
        result.append(0)
                


        return result