class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for val in logs:
            if val=="../" and len(stack)>0:
                stack.pop()
            elif val=="./":
                continue
            elif val!="../" and val!="./":
                stack.append(val)
        return len(stack)