class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # [indx, temp]

        # MONOTONIC STACK!
        # ---------------------------
        # A stack that always maintains a sorted order.
        # 
        #
        # Increasing: pop larger elements.
        # Decreasing: pop smaller elements.
        #
        # Used for Next/Previous Greater/Smaller Element problems in O(n).
        #
        # We usually store INDICES instead of values because indices
        # let us access both the value and its position later.

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = (i - stackI)
            stack.append([t, i])

        return result