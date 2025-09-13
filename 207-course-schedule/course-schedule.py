from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Step 1: Build graph
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def dfs(node):
            if state[node] == 1:   # cycle found
                return False
            if state[node] == 2:   # already checked
                return True
            
            state[node] = 1   # mark as visiting
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2   # mark as visited
            return True
        
        # Step 2: Check all courses
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True
