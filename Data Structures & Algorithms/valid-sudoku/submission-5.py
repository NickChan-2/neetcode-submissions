class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # could hash here i believe where we check 3 things.
        # col, row, box. if in seen return then false else walk through full list

        # could probably walk through each row we know exact starting point for each box too
        # range for boxes, box 1 cols[0,2], rows[0,2] so on so forth

        # actually better to do something where we keep track of num and what rows, boxes, cols it appears in
        seen_row = {"1": [], "2": [], "3": [], "4": [],
            "5": [], "6": [], "7": [], "8": [], "9": []}
        seen_col = {"1": [], "2": [], "3": [], "4": [], 
            "5": [], "6": [], "7": [], "8": [], "9": []}
        seen_box = {"1": [], "2": [], "3": [], "4": [], 
            "5": [], "6": [], "7": [], "8": [], "9": []}

        for r in range(len(board)):
            for c in range(len(board[0])):
                
                if board[r][c] == '.':
                    continue

                if r in seen_row[board[r][c]]:
                    return False
                else:
                    seen_row[board[r][c]] = [r]

                # check col
                if c in seen_col[board[r][c]]:
                    return False
                else:
                    seen_col[board[r][c]] = [c]
                
                if r < 3:
                    box = 1
                elif r >= 3 and r < 6:
                    box = 4
                else:
                    box = 7
                
                if c < 3:
                    pass
                elif c >= 3 and c < 6:
                    box += 1
                else:
                    box += 2

                # check box
                if box in seen_box[board[r][c]]:
                    return False
                else:
                    seen_box[board[r][c]] = [box]
        
        return True

                
                

                

                