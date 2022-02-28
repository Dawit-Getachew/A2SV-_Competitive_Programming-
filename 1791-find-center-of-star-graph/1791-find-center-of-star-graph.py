class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgeOne= edges[0][0]
        edgeTwo = edges[0][1]
        edgeOneCouner, edgeTwoCounter = 0, 0 
        for i in range(len(edges)):
            if edgeOne == edges[i][0] or edgeOne == edges[i][1]:
                edgeOneCouner+=1
            if edgeTwo == edges[i][0] or edgeTwo == edges[i][1]:
                edgeTwoCounter+=1
        return edgeOne if edgeOneCouner == len(edges) else edgeTwo