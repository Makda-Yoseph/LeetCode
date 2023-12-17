class UndergroundSystem:

    def __init__(self):
        self.checkin = {} # id - startstaion,t
        self.arrive = {} # startstat,endstat - trvlt,count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName,t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstat,startt = self.checkin[id]
        path = (startstat,stationName)
        if path not in self.arrive:
            self.arrive[path] = [0,0]
        self.arrive[path][0] += t - startt
        self.arrive[path][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg,count = self.arrive[startStation,endStation]
        return avg / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)