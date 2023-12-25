class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.t = timeToLive
        self.expire = defaultdict(int)
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expire[tokenId]= self.t + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.expire[tokenId] > currentTime:
            self.expire[tokenId] = currentTime + self.t

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for v in self.expire.values():
            if v > currentTime:
                count +=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)