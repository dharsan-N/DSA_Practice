# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root=self.reverse(root)
        return root
    def reverse(self,node):
        if not node:
            return None
        left=self.reverse(node.left)
        right=self.reverse(node.right)
        node.right,node.left=left,right
        return node