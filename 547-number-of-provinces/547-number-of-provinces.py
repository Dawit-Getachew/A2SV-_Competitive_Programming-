class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        rank  = [1 for _ in range(len(isConnected))]
        self.count = len(isConnected)
        
        def find(v):
            if (v == parents[v]):
                return v
            parents[v] =  find(parents[v])
            return parents[v]
        
        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                self.count -= 1
                if rank[pa] > rank[pb]:
                    parents[pb] = pa
                elif rank[pa] < rank[pb]:
                    parents[pa] = pb
                else:
                    parents[pb] = pa
                    rank[pa] += 1
                    
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    union(i,j)
                    
        return self.count
        
        
        