# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            rightEle = None
            for i in range(qLen):
                cur = q.popleft()

                if cur:
                    rightEle = cur.val
                    q.append(cur.left)
                    q.append(cur.right)

            if rightEle:
                res.append(rightEle)

        return res