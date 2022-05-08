class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res, visited = [], [0] * len(graph)
        def helperDfs(i):
            if visited[i]: 
                return visited[i] == 1            
            visited[i] = 2
            for j in graph[i]:
                if not helperDfs(j):
                    return False
            visited[i] = 1
            return True
        for i in range(len(graph)):
            if helperDfs(i):
                res.append(i)
        return res 
        
         