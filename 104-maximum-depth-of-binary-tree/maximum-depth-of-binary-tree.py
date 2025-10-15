# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(curr):
            if not curr:
                return 0
            left=dfs(curr.left)
            right=dfs(curr.right)
            
            
            return 1 + max(left,right)
        
        return dfs(root)