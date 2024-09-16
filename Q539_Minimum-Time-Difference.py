class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Turns hour to minutes
        # calculate the difference each time points and get the minmum number between(num, 24*60-num)
        minutes = []
        for i in range(len(timePoints)):
            HH, MM = timePoints[i].split(":")
            minutes += [int(HH)*60+int(MM)]
        minutes.sort()
        diff = []
        for i in range(len(minutes)-1):
            diff += [minutes[i+1]-minutes[i]]
        diff += [minutes[-1]-minutes[0]]
        return min(diff + [60*24-max(diff)])