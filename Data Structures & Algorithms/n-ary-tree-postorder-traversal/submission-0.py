"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        stack = [(root,False)]
        while stack:
            current_node,visited = stack.pop()
            if visited:
                result.append(current_node.val)
            else:
                stack.append((current_node,True))
                if current_node.children:
                    for child in reversed(current_node.children):
                        if child:
                            stack.append((child,False))
        return result