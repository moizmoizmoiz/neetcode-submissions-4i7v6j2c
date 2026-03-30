class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Each row must contain the digits 1-9 without duplicates.
        for row in board:
            print(row)
            count = Counter(row)
            del count['.']
            for c in count.values():
                if c > 1:
                    return False
                    break

        # Each col must contain the digits 1-9 without duplicates.    
        for c in range(9):
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,}
            for row in board:
               if row[c] != '.':
                numbers[row[c]] = numbers.get(row[c], 0) + 1
                if numbers[row[c]] > 1:
                    return False
                    break

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    
                    seen.add(board[row][col])
 

        return True