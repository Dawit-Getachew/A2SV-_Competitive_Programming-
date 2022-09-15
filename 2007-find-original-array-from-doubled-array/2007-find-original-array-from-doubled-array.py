class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        current = deque()
        result = []
        for num in changed:
            if current and current[0] * 2 == num:
                result.append(current.popleft())
            else:
                current.append(num)
        return result if not current else []