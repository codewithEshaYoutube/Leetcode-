class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, trees are same
        if not p and not q:
            return True
        
        # If one is None and other is not
        if not p or not q:
            return False
        
        # Check current node value and subtrees
        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
