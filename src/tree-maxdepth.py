from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        else:
            return max( self.maxDepth(root.left) + 1,
                        self.maxDepth(root.right) + 1)

t15=TreeNode(15)
t7=TreeNode(7)
t91=TreeNode(91,t7)

t20=TreeNode(20,t15,t91)
t9=TreeNode(9)
t3=TreeNode(3, t91, t20)

s = Solution()
print(s.maxDepth(t91))
