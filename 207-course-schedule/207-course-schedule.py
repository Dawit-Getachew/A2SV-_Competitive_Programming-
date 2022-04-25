class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parent, indegree = defaultdict(list), [0] * numCourses
        queue = deque()
        for course, preReq in prerequisites:
            indegree[course] += 1
            parent[preReq].append(course)
            
        for i in range(numCourses):
            if indegree[i] == 0 and i in parent:
                queue.append(i)
                
        while queue:
            Course = queue.popleft()
            for Next in parent[Course]:
                indegree[Next] -= 1
                if indegree[Next] == 0:
                    queue.append(Next)

        return max(indegree) == 0