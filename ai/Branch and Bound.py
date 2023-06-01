#Branch and Bound

def printsolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
        
def is_safe(row, col, UD, LD, rowlookup, UDlookup, LDlookup):
    if(UDlookup[UD[row][col]] or LDlookup[LD[row][col]] or rowlookup[row]):
        return False
    return True
    
def solveNQueensUtil(board, col, UD, LD, rowlookup, UDlookup, LDlookup):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(i, col, UD, LD, rowlookup, UDlookup, LDlookup):
            board[i][col] = "Q"
            rowlookup[i] = True
            UDlookup[UD[i][col]] = True
            LDlookup[LD[i][col]] = True
            
            if solveNQueensUtil(board, col+1, UD, LD, rowlookup, UDlookup, LDlookup):
                return True
         
            board[i][col] = "-"
            rowlookup[i] = False
            UDlookup[UD[i][col]] = False
            LDlookup[LD[i][col]] = False
        
    return False

def SolveNQuees():
    board = [["-" for _ in range(N)] for _ in range(N)]
    UD = [["-" for _ in range(N)] for _ in range(N)]
    LD = [["-" for _ in range(N)] for _ in range(N)]
    rowlookup = [False] * N
    x = 2 * N -1
    UDlookup = [False] * x
    LDlookup = [False] * x
    
    for rr in range(N):
        for cc in range(N):
            UD[rr][cc] = rr+cc
            LD[rr][cc] = rr-cc+N-1
    
    if not solveNQueensUtil(board, 0, UD, LD, rowlookup, UDlookup, LDlookup):
        print("Solution Doesn't Exist !!!")
            
    printsolution(board)
    return True
    
N = int(input("Enter the board size : "))
SolveNQuees()