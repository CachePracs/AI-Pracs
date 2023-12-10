
class nqBoard:
    
    def __init__(self, n):
        self.n=n
        self.board=[[0 for i in range(self.n)]for i in range(self.n)]

    def solveNQUtil(self, c):
        if(c >= self.n):
            return True
        for i in range(self.n):
            if(self.isSafe(i, c)):
                self.board[i][c] = 1
                if(self.solveNQUtil(c+1) == True):
                    return True

            self.board[i][c] = 0

        return False

    def printNQ(self):
        print("\n")
        for i in range(self.n):
            print("\t", end="")
            for j  in range(self.n):
                print(self.board[i][j], end=" ")
            print()
        #print("\n")

    def isSafe(self, r, c):
        for i in range(c):
            if(self.board[r][i] == 1):
                return False
        '''
        for i in range(r):
            if(self.board[i][c] == 1):
                return False
        '''  
        for i,j in zip(range(r, -1, -1), range(c, -1, -1)):
            if(self.board[i][j] == 1):
                return False

        for i,j in zip(range(r, self.n, 1), range(c, -1, -1)):
            if(self.board[i][j] == 1):
                return False
    
        return True

    def solveNQ(self):
        print("For ", self.n, " Queens Solution is")
        if(self.solveNQUtil(0) == False):
            print("Solution Doesn't Exists...")
            return False
        self.printNQ()
        return True

n = int(input("Enter number of Queens: "))
qb1 = nqBoard(n)
qb1.solveNQ()