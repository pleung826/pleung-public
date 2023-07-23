from typing import Optional

#         5
#        /  \
#      3     3
#     / \    / \
#    2   1  1   2
#   /\   /\  /\  /\
#  1  0  1 0 0 1 0 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrder(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            pass
        else:
            self.inOrder(root.left)
            print(root.val, end=' ')
            self.inOrder(root.right)

    def isSymmetrical(self, root):
        queue=[]
        queue.append(root)
        level=0
        while len(queue) > 0:
            string=''
            for i in range(0, len(queue)):
                node=queue.pop(0)
                string=string + str(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            isPalindrome = self.palindrome(string)
            print(f'level={level} ', string, isPalindrome)
            if not isPalindrome or len(string) != pow(2, level):
                return False
            level = level + 1

        return True

    def palindrome(self, str):
        i = 0;
        j = len(str)-1
        while i < j:
            if str[i] != str[j]:
                return False
            i = i + 1
            j = j - 1
        return True

t31 = TreeNode(3,None,None); t32 = TreeNode(4,None,None)
t33 = TreeNode(4,None,None); t34 = TreeNode(3,None,None)

t21 = TreeNode(2,t31,t32)
t22 = TreeNode(2,t33,t34)
t1 = TreeNode(1,t21,t22)

s=Solution()
# s.inOrder(t1)
# print()
# print(s.palindrome("3 2 4 1 4 2 3"))
# print(s.palindrome("a0"))
# print(s.palindrome("abc"))
# print(s.palindrome("abcba"))
print("symmetrical=", s.isSymmetrical(t1))