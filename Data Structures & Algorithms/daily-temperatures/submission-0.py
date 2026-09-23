class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = []
        n = len(temp)
        answer = [0] * n
        
        for i, t in enumerate(temp):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append((t, i))

        return answer