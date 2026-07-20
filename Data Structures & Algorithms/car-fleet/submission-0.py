class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)
        print(cars)
        for car in cars:
            carPosition, carSpeed = car
            time = (target - carPosition)/carSpeed
            if not fleets or time > fleets[-1]:        
                fleets.append(time)
        return len(fleets)
                