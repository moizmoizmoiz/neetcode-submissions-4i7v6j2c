class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        

        fleet = 0
        stack = []
        cars = sorted(zip(pos, speed), reverse=True) #Neetcode used list comprehensio
        
        
        for c in cars:
            time = (target - c[0]) / c[1] 

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: # we keep the biggest ones in order
                stack.pop()
        
        print(stack)
        return(len(stack))




        