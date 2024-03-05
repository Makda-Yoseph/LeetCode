class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        start = []
        seen = set()
        for j in range(len(board)):
            for k in range(len(board[0])):
                if board[j][k] == word[0]:
                    start.append([j,k])
        
        def backtrack(r,c,s):
            if len(word) == len(path):
                return True
            if r<0 or r >= len(board):
                return 
            if c<0 or c>=len(board[0]):
                return 
    
            if s>=len(word):
                return 
            if word[s] == board[r][c] and (r,c) not in seen:
                path.append(board[r][c])
                seen.add((r,c))
                if backtrack(r+1,c,s+1):
                    return True
                if backtrack(r-1,c,s+1):
                    return True
                if backtrack(r,c+1,s+1):
                    return True
                if backtrack(r,c-1,s+1):
                    return True
                path.pop()
                seen.remove((r,c))
           
        
        for r,c in start:
            if backtrack(r,c,0) :
                return True
            
        else:
            return False
        


        