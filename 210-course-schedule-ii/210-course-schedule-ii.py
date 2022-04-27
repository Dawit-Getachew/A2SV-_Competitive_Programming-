class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {}
        numPreReq = {}
        for (a,b) in prerequisites:
            preReq[b] = preReq.get(b,[]) + [a]
            numPreReq[a] = numPreReq.get( a, 0 ) + 1
        queue, response = collections.deque(), []
        for i in range (numCourses):
            if i not in numPreReq:
                response.append(i)
                queue.append(i)
        while queue:
            course = queue.popleft()
            for nbr in preReq.get(course, []):
                numPreReq[nbr] -= 1
                if numPreReq[nbr] == 0:
                    queue.append(nbr)
                    response.append(nbr)
        return [] if len(response) != numCourses else response