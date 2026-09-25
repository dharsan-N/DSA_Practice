# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p,q)
    def compare(self,h1,h2):
        if not h1 and not h2:
            return True
        if (h1 and h2) and (h1.val!=h2.val):
            return False
        if (not h1 and h2) or (h1 and not h2):
            return False
        return self.compare(h1.left,h2.left) and self.compare(h1.right,h2.right)