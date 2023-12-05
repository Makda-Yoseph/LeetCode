class Solution(object):
    def escapeGhosts(self, ghosts, target):
        me = abs(target[0] )+ abs(target[1])
        for i in range(len(ghosts)):
            g = 0
            g = abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1])
            if g <= me:
                return False
                break
        return True