k= int(input())
chessboard=[[0 for _ in range(k)] for _ in range(k)]

def isAttacking(i,j):
    for q in range (k):
        if chessboard[i][q] ==1 or chessboard[q][j] ==1:
            return(True)
    for l in range (k):
        for m in range(k):
            if l+m == i+j and chessboard[l][m] ==1:
                return(True)
            if l-m == i-j and chessboard[l][m] ==1:
                return(True)
    return(False)

def nQueens(n):
    if n==0:
        return(True)
    for i in range(k):
        for j in range(k):
            if not isAttacking(i,j) and chessboard[i][j]==0:
                chessboard[i][j]=1
                if nQueens(n-1):
                    return(True)
                chessboard[i][j]=0
    for u in chessboard:
        print(u)
    return(False)
   


print(nQueens(k))