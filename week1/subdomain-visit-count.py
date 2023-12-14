class Solution(object):
    def subdomainVisits(self, cpdomains):
        count = {}
        output = []
        for web in cpdomains:
            page = web.split()
            i = len(page[1])-1
            while i >= 0:
                if  i==0:
                    if page[1][i:] not in count:
                        count[page[1][i:]] = int(page[0])
                    else:
                        count[page[1][i:]] += int(page[0] )

                elif page[1][i] == '.' :
                    if page[1][i+1:] not in count:
                        count[page[1][i+1:]] = int(page[0])
                    else:
                        count[page[1][i+1:]] +=int( page[0] )
                i -=1
        for key,val in count.items():
            full = str(val) + " " + key
            output.append(full)
        return output
            




        