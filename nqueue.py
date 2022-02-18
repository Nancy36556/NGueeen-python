
global N
N=4
def printSol(board):
    for row in board :
        print(row)
def isSave(board , row ,col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row ,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
         return False
    for i,j in zip(range(row ,N,1), range(col,-1,-1)):
        if board[i][j] == 1:
         return False
    return True
def solveQu(board, col):
    if col >= N:
      return True
    for i in range(N):
        if isSave(board , i , col):
            board[i][col] = 1
            if solveQu(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False
def sol():
    board =[[0 , 0 , 0 ,0],
            [0 , 0 , 0 ,0],
            [0 , 0 , 0 ,0],
            [0 , 0 , 0 ,0]
            ]
    if solveQu(board,0)==False:
        print("sol doesn't exist")
        return False
    printSol(board)
    return True
sol()
        
            
