class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(left, right):
            # both empty → symmetric
            if not left and not right:
                return True
            
            # one empty → not symmetric
            if not left or not right:
                return False
            
            # values must match
            if left.val != right.val:
                return False
            
            # mirror comparison
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)
