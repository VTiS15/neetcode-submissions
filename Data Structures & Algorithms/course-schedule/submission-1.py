from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Returns True if it is possible to finish all courses, otherwise return False.

        We can model the relationships between courses with a directed graph
        where every edge points to a course from one of its prerequisites. Then it is
        possible to finish all courses if, and only if, there is no cycle in the graph.
        Here we use Kahn's algorithm to solve the problem.

        Args:
            numCourses (int): The number of courses.
            prerequisites (List[List[int]]): An array where prerequisites[i] = [a, b]
                indicates that you must take course b first if you want to take course a.
        
        Returns:
            bool: True if it is possible to finish all courses, otherwise return False.

        """
        # Create an adjacency list
        adj = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        # Create a list to store indegrees of all vertices
        indegree = [0] * numCourses  # Initialize all indegrees as 0
        for course, _ in prerequisites:
            indegree[course] += 1

        # Create a queue and enqueue all vertices with indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0  # Initialize count of visited vertices
        # One by one dequeue vertices from queue and enqueue adjacent node if indegree of adjacent node becomes 0
        while queue:
            u = queue.pop()
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            count += 1
        
        return count == numCourses  # There is no cycle iff count == numCourses
        