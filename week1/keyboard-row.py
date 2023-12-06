class Solution(object):
    def findWords(self, words):
        exist = []
        
        for word in words:
            count =0
            if word[0].lower() in  "qwertyuiop":
                for i in range(len(word)):
                    if word[i].lower() in "qwertyuiop":
                        count +=1
                    else:
                        break
            if word[0].lower() in "asdfghjkl":
                for i in range(len(word)):
                    if word[i].lower() in "asdfghjkl":
                        count +=1
                    else:
                        break
            if word[0].lower() in "zxcvbnm":
                for i in range(len(word)):
                    if word[i].lower() in "zxcvbnm":
                        count+=1
                    else:
                        break
            if count == len(word):
                exist.append(word)
        return exist

                