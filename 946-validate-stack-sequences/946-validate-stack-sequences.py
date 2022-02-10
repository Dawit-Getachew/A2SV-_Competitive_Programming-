class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ans = deque()
        for elem in pushed:
            ans.append(elem)
            while ans and popped and ans[-1] == popped[0]:
                popped.pop(0)
                ans.pop()
        return True if not popped else False