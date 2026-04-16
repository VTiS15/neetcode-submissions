from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        indegree = [0] * numCourses
        for course, _ in prerequisites:
            indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            u = queue.pop()
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            count += 1
        
        return count == numCourses
        