class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        if len(isConnected) == 1: return 1

        out = 0

        visited = set()
        visiting = set()

        def check(node): 
            nonlocal out

            if node in visited: 
                return 
            if node in visiting: 
                return 

            visiting.add(node)

            for i in range(len(isConnected[node])): 
                if isConnected[node][i]: 
                    check(i)
            
            visited.add(node)
            visiting.remove(node)
            
        for i in range(len(isConnected)):
            if i not in visited:
                out = out + 1 
                check(i)
        
        return out
        