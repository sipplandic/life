# Import the cell class

from cell import cell

# Define a board class

class board:
    def __init__(self, rows, cols):
        ## excluding as this is unknown value to me
        # super(, self).__init__()
        ## if uncommented... pls explain the purpose for future reference
        self.boardspace = [] # intialize a blank list
        self.rows = rows
        self.cols = cols
        # Create a 2d list of cells of dimension rows x cols
        for row in range(0,self.rows):
            self.boardspace.append([])
            for col in range(0,self.cols):
                self.boardspace[row].append(cell())


    def access(self,row,col):
        row = row%self.rows
        col = col%self.cols

        return self.boardspace[row][col]

    def disp(self): # this function needs to do basic printing of the 0/1s
        s = ''
        for row in range(0,self.rows):
            for col in range(0,self.cols):
                if self.access(row,col).isalive == 1:
                    s = s + 'x '
                else:
                    s = s + '  '
            s = s + '\n'
        print(s)

    def stork(self,row,col):
        self.access(row,col).live()

    def reaper(self,row,col):
        self.access(row,col).die()

    def neighbors(self,row,col):
        numNeighbors = 0
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                numNeighbors = numNeighbors + self.access(i,j).isalive
        numNeighbors = numNeighbors - self.access(row,col).isalive
        return numNeighbors

    def evolve(self):
        newspace = []

        for row in range(0,self.rows):
            newspace.append([])
            for col in range(0,self.cols):
                newspace[row].append(cell())
                numNeighbors = self.neighbors(row,col)
                if self.access(row,col).isalive == 1:
                    if numNeighbors == 2 or numNeighbors == 3:
                        newspace[row][col].live()
                else:
                    if numNeighbors == 3:
                        newspace[row][col].live()

        assert self.rows == len(newspace)
        assert self.cols == len(newspace[0])
        self.boardspace = newspace
