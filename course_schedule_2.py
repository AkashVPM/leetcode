from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        d = defaultdict(list)

        for u,v in prerequisites: 
            d[u].append(v)
        
        visited = set()
        visiting = set()
        order = []

        def visit (course): 
            if course in visiting: 
                return False
            if course in visited: 
                return True
            
            visiting.add(course)

            for prereq in d[course]: 
                if not visit(prereq): return False
            
            order.append(course)
            visiting.remove(course)
            visited.add(course)

            return True
        

        for course in range(numCourses): 
            if not visit(course): return []
        
        return order