class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # know the car arrival time
        # Group the cars respect of the ahead car
        # First sort by the position
        # Find the ascending number,  
        # arrival time => [10, 9, 7, 6, 11, 10, 13]
        # Group1 => [10, 9, 7, 6]
        # Group2 => [11, 10]
        # Group3 => [13]
        arrivals = [(target-p)/s for p, s in sorted(zip(position, speed), reverse=True)]
        groups = 0
        last_seen = 0
        for arrival in arrivals:
            if arrival > last_seen:
                last_seen = arrival
                groups += 1
        return groups

