class Solution(object):
    def findDuplicate(self, paths):
        output= []
        
        content = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            root = path[0]
            for c in path[1:]:
                c = c.split(".txt")
                num = c[0]
                cont = c[1]
                content[cont].append((root,num))
        for key,val in content.items():
            if len(val)> 1:
                temp = []
                for r,n in val:
                    temp.append(r + '/' + n+".txt")
                output.append(temp)
        return output
            

        