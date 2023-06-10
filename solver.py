from main import board
n=len(board)


class Cell:
    def __init__(self, row: int, col: int, checked=False) -> None:
        self.row=row
        self.col=col
        self.checked=checked
        self.value='*'

    def look(self)->tuple:
        '''returns (count_of_mines, not_checked_count, other_checked_count)'''
        mines, nc, oc = 0,0,0
        for i in range(self.row-2,self.row+1):
            if i<0 or i>= n: continue
            for j in range(self.col-2,self.col+1):
                if j<0 or j >= n or i+1==self.row and j+1==self.col: continue
                if boardview[i][j].value==9:
                    mines+=1
                elif boardview[i][j].value=='*':
                    nc+=1
                else:
                    oc+=1
        return (mines, nc, oc)
    
    def open_cells(self):
        for i in range(self.row-2,self.row+1):
            if i<0 or i>= n: continue
            for j in range(self.col-2,self.col+1):
                if j<0 or j >= n : continue
                if boardview[i][j].value=='*':
                    boardview[i][j].click()

    def click(self):
        if board[self.row-1][self.col-1]==9:
            raise Exception("LOSSEEEEERRRR")#Never
        self.checked=True
        self.value=board[self.row-1][self.col-1]

    def print(self):
        print(self.value, end=', 'if self.col < n else '\n')



boardview=[[Cell(i+1,j+1) for j in range(n)] for i in range(n)]


# test
boardview[3][3].open_cells()
print(boardview[3][4].row, boardview[3][4].col)
print(boardview[3][4].look())
for i in range(n):
    for j in range(n):
        boardview[i][j].print()
