class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n is number of cars 
        # two arrays position and speed - length n 
        # target = 10, position = [1,4], speed = [3,2]

        cars = []

        for i, pos in enumerate(position):
            cars.append([pos, speed[i]])
        cars.sort(reverse = True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)