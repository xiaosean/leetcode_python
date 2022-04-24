class UndergroundSystem:

    def __init__(self):
        self.passengers = {}
        self.travels = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        from_, to_, cost = self.passengers[id][0], stationName, t-self.passengers[id][1]
        hash_str = f"{from_} {to_}"
        if hash_str in self.travels:
            avg_cost, n = self.travels[hash_str][0], self.travels[hash_str][1]
            total_cost = avg_cost*n + cost
            n += 1
            self.travels[hash_str] = [total_cost/n, n]
        else:
            self.travels[hash_str] = [cost, 1]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        hash_str = f"{startStation} {endStation}"
        return self.travels[hash_str][0] if hash_str in self.travels else None


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)