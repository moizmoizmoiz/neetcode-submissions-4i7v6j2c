class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # VERY VERY NAIVE DUMBASS 2 POINTER STYLE SOLUTION WITH O(n^2)
        
        
        # A cleaner approach is to initialise the result array with zeros:
        # 
        # result = [0] * len(temperatures)
        #
        # Instead if appending 0s  
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count += 1
                    result[i] = count 
                    print(count)
                    break
                else:
                    count += 1


  

                


        return result