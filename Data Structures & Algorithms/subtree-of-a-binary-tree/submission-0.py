# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subroot:
            return True
        
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p and q and p.val == q.val:
                return is_same_tree(p.left,q.left) and is_same_tree(p.right,q.right)
        
        if is_same_tree(root,subroot):
            return True
        return (self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot))
        