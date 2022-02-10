from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minLevelSum(root):
    q = Queue()
    q.put(root)
    minSum = float('inf')
    curLevel, minLevel = 0, 0
    while q.qsize():
        tempList = []

        for _ in range(0, q.qsize()):
            curr = q.get()
            tempList.append(curr.data)
            if curr.left: q.put(curr.left)
            if curr.right: q.put(curr.right)

        if sum(tempList ) < minSum:
            minSum = sum(tempList)
            minLevel = curLevel

        curLevel += 1
    return minLevel