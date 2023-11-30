class Solution(object):
    def interpret(self, command):
        s = ""
        for i in range(len(command)):
            j = i+1
            if command[i] =='G':
                s +="G"
            elif command[i] =='(':
                if command[j] == ')':
                    s += "o"
                    pass
                else:
                    s+="al"
                    continue
        return s
                

        
        