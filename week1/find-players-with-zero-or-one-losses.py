class Solution(object):
    def findWinners(self, matches):
        lossers = {}
        w ,l = [],[]
        for winner,loser in matches:
            lossers[winner] = lossers.get(winner,0)
            lossers[loser] = lossers.get(loser,0)+1
        for player,loss in lossers.items():
            if loss == 0:
                w.append(player)
            if loss == 1:
                l.append(player)
        return(sorted(w),sorted(l))
        
