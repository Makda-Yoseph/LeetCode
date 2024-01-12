class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
     
        basket = {}
        r,l,ct,ma = 0,0,0,0
        while r < len(fruits):
            # if  len(basket)<=2 :
            basket[fruits[r]] = basket.get(fruits[r],0)+1
            if len(basket) ==3:
                ma = max(ma,r-l)
                while len(basket)>2:
                    basket[fruits[l]] -=1
                    if basket[fruits[l]] == 0:
                        del basket[fruits[l]]
                    l+=1
            r+=1
                
        ma = max(ma,r-l)
        return ma

                


                

