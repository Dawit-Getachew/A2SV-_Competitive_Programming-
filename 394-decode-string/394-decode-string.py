class Solution:
    def decodeString(self, s: str) -> str:
        stack, num = [], 0
        result = ""
        for val in s:
            if val.isdigit():
                num = num*10+int(val)    
            elif val=="[":
                stack.append(result)
                stack.append(num)
                result, num = "", 0
            elif val=="]":
                poppedNum, poppedString = stack.pop(), stack.pop()
                result = poppedString + poppedNum*result
            else:
                result+=val
        return result