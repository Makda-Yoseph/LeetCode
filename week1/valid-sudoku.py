class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = 0
        
        for i in board:
            occur = {}
            for k in i:
                if k != ".":
                    occur[k] = occur.get(k,0) +1
            for v in occur.values():
                if v>1:
                    flag = 1
        for j in  zip(*board):
            opp= {}
            for k in j:
                if k != ".":
                    opp[k] = opp.get(k,0) +1
            for v in opp.values():
                if v>1:
                    flag = 1
        print(opp)
        for i in range(0, 9, 3):  
            for j in range(0, 9, 3): 
                acc= {}
                for k in range(3):
                    for l in range(3):
                        if board[k+i][l+j] != ".":
                            acc[board[k+i][l+j]] = acc.get(board[k+i][l+j],0) +1
                for v in acc.values():
                    if v>1:
                        flag = 1
                print(acc)
        if flag == 1:
            return False
        else:
            return True

        