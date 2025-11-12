class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        c=defaultdict(list)
        r=defaultdict(list)
        s=defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    if int(board[i][j]) in c[i]:
                        return False
                    if int(board[i][j]) in r[j]:
                        return False
                    if int(board[i][j]) in s[(i//3,j//3)]:
                        return False
                    c[i].append(int(board[i][j]))
                    r[j].append(int(board[i][j]))
                    s[(i//3,j//3)].append(int(board[i][j]))
        return True