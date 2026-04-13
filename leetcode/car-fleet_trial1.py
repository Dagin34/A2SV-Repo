class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        
        fleet = 0
        max_time = 0
        for pos, spd in reversed(cars):
            time = (target - pos) / spd
            
            if time > max_time:
                fleet += 1
                max_time = time
        
        return fleet