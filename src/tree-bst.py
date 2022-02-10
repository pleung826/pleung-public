from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        elif root.left != None and root.left.val >= root.val:
            return False
        elif root.right != None and root.right.val <= root.val:
            return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right)

# t1=TreeNode(1)
# t3=TreeNode(3)
# t6=TreeNode(6)
# t4=TreeNode(4,t3,t6)
# t5=TreeNode(5,t1,t4)
t1=TreeNode(2)
t2=TreeNode(5)
t3=TreeNode(4,t1,t2)


s=Solution()
print(s.isValidBST(t3))