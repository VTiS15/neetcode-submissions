from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Calculate the indegrees
        indegrees = [0] * numCourses
        for course, _ in prerequisites:
            indegrees[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        res = []
        while q:
            s = q.popleft()
            res.append(s)
            for v, u in prerequisites:
                if u == s:
                    indegrees[v] -= 1
                    if indegrees[v] == 0:
                        q.append(v)
        
        if len(res) != numCourses:
            return []
        return res