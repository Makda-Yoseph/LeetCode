class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = row
        for i in image:
            i.reverse()
            for j in range(col):
                if i[j] ==1:
                    i[j]= 0
                else:
                    i[j] = 1
        return image
                    


        