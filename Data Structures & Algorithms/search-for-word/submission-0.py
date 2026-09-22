class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(r, c, i):

            # found every letter
            if i == len(word):
                return True

            # outside board
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False

            # wrong letter
            if board[r][c] != word[i]:
                return False

            # make choice
            temp = board[r][c]
            board[r][c] = '0'

            # explore choices
            found = (
                search(r + 1, c, i + 1) or
                search(r - 1, c, i + 1) or
                search(r, c + 1, i + 1) or
                search(r, c - 1, i + 1)
            )

            # BACKTRACK: undo choice
            board[r][c] = temp

            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(r, c, 0):
                    return True

        return False