class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs=collections.defaultdict(set)
        cs=collections.defaultdict(set)
        sq=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in rs[r] or board[r][c] in cs[c] or board[r][c] in sq[(r//3,c//3)]:
                    return False
                rs[r].add(board[r][c])
                cs[c].add(board[r][c])
                sq[(r//3,c//3)].add(board[r][c])
        return True