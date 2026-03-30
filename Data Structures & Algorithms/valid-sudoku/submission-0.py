class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bL = len(board)
        for row in range(bL) :
            s = set()
            for col in range(bL) :
                v = board[row][col]
                if v == '.' :
                    continue
                if v in s :
                    return False
                s.add(v)

        for column in range(bL) :
            s = set()
            for row in range(bL) :
                v = board[row][column]
                if v == '.' :
                    continue
                if v in s :
                    return False
                s.add(v)
            

        for row in range(0, 9, 3) :
            for col in range(0, 9, 3) :
                s = set()
                for i in range(row, row+3) :
                    for j in range(col, col+3) :
                        v = board[i][j]
                        if v == '.' :
                            continue
                        if v in s :
                            return False
                        s.add(v)

        return True