class Solution:
    def generateParenthesis(self, n):
        lst = []
        stack = []
        openP = 0
        closeP = 0
        self.generateParanthesisHelper(n, lst,stack, openP, closeP)
        return lst
    
    def generateParanthesisHelper(self, n, lst, stack, openP, closeP):
        if openP == n and closeP == n:
            lst.append("".join(stack))
            return
        if openP < n:
            stack.append("(")
            self.generateParanthesisHelper(n, lst, stack, openP+1, closeP)
            stack.pop()
        if closeP < openP:
            stack.append(")")
            self.generateParanthesisHelper(n, lst, stack, openP, closeP+1)
            stack.pop()

s=Solution()
print(s.generateParenthesis(4))
