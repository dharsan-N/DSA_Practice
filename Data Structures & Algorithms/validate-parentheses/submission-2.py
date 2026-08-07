class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open="[{("
        dic={']':"[","}":"{",")":"("}
        for x in s:
            if x in open:
                stack.append(x)
            elif stack and dic[x]==stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        print(stack)
        return not stack