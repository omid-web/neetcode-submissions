# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = []
        heights = defaultdict(int)
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack[-1]
            if node.right and node.right not in heights:
                node = node.right
            else:
                node = stack.pop()
                left, right = heights[node.left], heights[node.right]
                if abs(left - right) > 1:
                    return False
                
                heights[node] = 1 + max(left, right)
                node = None
        
        return True