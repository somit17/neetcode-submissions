# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #dfs approach
        if not root:
            return []
        result = []
        def dfs_traversal_post_order(root: Optional[TreeNode]):
            if not root:
                return None
            dfs_traversal_post_order(root.left)
            dfs_traversal_post_order(root.right)
            result.append(root.val)
             
        dfs_traversal_post_order(root)
        return result
