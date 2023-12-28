class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [['0']*n for _ in range(m)]
        for i,j in walls:
            mat[i][j] = 'W'
        for i,j in guards:
            mat[i][j] = 'G'
        for i in range(m):
            flag = False
            for j in range(n):
                if mat[i][j] =="G":
                    flag = True
                    print(0)
                elif mat[i][j] == "W":
                    flag = False
                    print(1)
                elif flag==True:
                    mat[i][j] ="x"
                    print(2)
            flag = False
            for j in range(n-1,-1,-1):
                if mat[i][j] =="G":
                    flag = True
                elif mat[i][j] == "W":
                    flag = False
                elif flag :
                    mat[i][j] = "x"
        for j in range(n):
            flag = False
            for i in range(m):
                if mat[i][j] =="G":
                    flag = True
                elif mat[i][j] == "W":
                    flag = False
                elif  flag:
                    mat[i][j] ="x"
            flag = False
            for i in range(m-1,-1,-1):
                if mat[i][j] =="G":
                    flag = True
                elif mat[i][j] == "W":
                    flag = False
                elif flag :
                    mat[i][j] = "x"
        
        print(mat)
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]=="0":
                    count +=1
        return count


            

        