# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        dq = deque([root])

        while dq:
            right_side = None
            level_size = len(dq)

            for i in range(level_size):
                node = dq.popleft()
                if node:
                    right_side = node
                    dq.append(node.left)
                    dq.append(node.right)
            if right_side:
                res.append(right_side.val)
        
        return res
        
        return result