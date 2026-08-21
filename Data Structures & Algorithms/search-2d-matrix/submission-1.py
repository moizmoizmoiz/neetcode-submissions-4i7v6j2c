class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        


        def hunter(row: List[int], target: int) -> bool:
            l, r = 0, len(row) -1

            while l <= r:
                m = (l+r) // 2

                if row[m] == target:
                    return True
                elif row[m] > target: # number is in the lower bounds
                    r = m - 1
                else: # number is in the upper bounds
                    l = m + 1 
            return False
        


        def triangulate(matrix: List[List[int]], target: int) -> int | None:

            l = 0
            r = len(matrix) - 1

            while l <= r:
                m = (l + r) //2

                if matrix[m][0] <= target and matrix[m][-1] >= target:
                    return m
                elif matrix[m][0] > target:
                    r = m - 1
                else:
                    l = m + 1

            return None


        row_indx = triangulate(matrix, target)

        if row_indx is not None:
           return hunter(matrix[row_indx], target)
        else:
            return False



        
