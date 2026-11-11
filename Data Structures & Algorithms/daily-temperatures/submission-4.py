class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [70, 65, 72, 75]
                #    i =   0   1   2   3
        stack = []
        n = len(temperatures)
        res = [0] * len(temperatures)

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res