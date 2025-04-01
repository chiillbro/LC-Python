from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the mapping: course -> list of prerequisites.
        prereq_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        # Separate arrays for visited status and recursion stack status.
        visited = [False] * numCourses
        onStack = [False] * numCourses
        courseOrder = []
        
        def dfs(course: int) -> bool:
            # Mark the course as visited and add it to the recursion stack.
            visited[course] = True
            onStack[course] = True
            
            for prereq in prereq_map[course]:
                if not visited[prereq]:
                    if not dfs(prereq):
                        return False  # Cycle detected in the DFS subtree.
                elif onStack[prereq]:
                    return False  # Found a cycle.
            
            # Append the course once all its prerequisites are processed.
            courseOrder.append(course)
            onStack[course] = False  # Remove from the recursion stack.
            return True
        
        for course in range(numCourses):
            if not visited[course]:
                if not dfs(course):
                    return []  # Cycle detected; no valid course order.
        
        # The current order is reversed relative to the desired order.
        # Because we add courses after processing prerequisites,
        # reversing will give a valid ordering.
        return courseOrder
