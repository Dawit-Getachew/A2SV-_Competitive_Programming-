class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate, size = list(senate), len(senate)
        rIndex = deque([i for i in range(size) if senate[i] == 'R'])
        dIndex = deque([i for i in range(size) if senate[i] == 'D'])
        while rIndex and dIndex:
            r, d = rIndex.popleft(), dIndex.popleft()
            if r > d:
                dIndex.append(size+d)
            else:
                rIndex.append(size+r)
        if not rIndex:
            return "Dire"
        return "Radiant"