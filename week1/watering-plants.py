class Solution(object):
    def wateringPlants(self, plants, capacity):
        oc = capacity
        ct = 0
        for i in range(len(plants)):
            if plants[i] <= capacity:
                ct +=1
                capacity -= plants[i]
            else:
                
               
                ct += 2*i +1 
                capacity = oc
                capacity -= plants[i]
                
        return ct

        