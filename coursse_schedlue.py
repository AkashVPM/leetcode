from collections import defaultdict
class Solution:
      def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        if len(prerequisites) < 1 : return True

        d = defaultdict(list)

        for course, prereq in prerequisites: 
            d[course].append(prereq)

        seen = set()
        for course, prereq in d.items(): 
            seen.add(course)
            for i in prereq:
                if i not in d: 
                    continue
                if i in seen: 
                    for j in d[i]: 
                        if j in seen: 
                            return False
                if course in d[i]: 
                    return False
                    
        return True
      
      def canFinish_optimal(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        if len(prerequisites) < 1 : return True

        d = defaultdict(list)

        for course, prereq in prerequisites: 
            d[course].append(prereq)
        
        visiting = set()
        visited = set()

        def visit(course): 
            if course in visiting: 
                return False 
            if course in visited: return True
            
            visiting.add(course)
           
            for preq in d[course]: 
                if not visit(preq): return False

            visiting.remove(course)
            visited.add(course)
            return True


        for course in range(numCourses): 
            if not visit(course): return False 
        
        return True