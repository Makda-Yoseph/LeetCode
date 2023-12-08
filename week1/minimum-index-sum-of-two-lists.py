class Solution(object):
    def findRestaurant(self, list1, list2):
        mini = 2**32 -1
        res = []
        w1 = {word:index for index,word in enumerate(list1)}
        w2 = { word: index for index,word in enumerate(list2)}
        for word in list1:
            if word in list2:
                d = w1[word] + w2[word]
                if d < mini:
                    if len(res) == 0:
                        res.append(word)
                    else:
                        res = []
                        res.append(word)
                elif d == mini:
                    res.append(word)
                else:
                    continue
                mini = min(mini,d)
        return res

        


                         


        



        