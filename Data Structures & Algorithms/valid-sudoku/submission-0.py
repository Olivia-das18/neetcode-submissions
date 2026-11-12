class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows    =    [set() for _ in range(9)]
        cols =       [set() for _ in range(9)]
        boxes   =    [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                boxes_index = (row//3)*3 +(col//3)

                if digit ==".":
                 continue 
                if (digit in rows[row] or
                    digit in cols[col] or
                    digit in boxes[boxes_index]):
                    return False

                else:
                   rows[row].add(digit)
                   cols[col].add(digit)
                   boxes[boxes_index].add(digit)
        return True


            






    
       