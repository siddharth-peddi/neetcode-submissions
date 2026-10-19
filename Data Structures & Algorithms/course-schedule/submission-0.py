from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * (numCourses)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        completed = 0 

        while queue:
            course = queue.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return completed == numCourses