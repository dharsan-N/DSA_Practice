# Definition for a binary tree node.
# class TreeNod             e:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.l=[]  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans=[]
        node =self.match(root,subRoot.val)
        for x in self.l:
            ans.append(self.same(x,subRoot))
        if any(ans):
            return True
        else:
            return False
    def match(self,node,val):
        if not node:
            return 0
        if node.val==val:
            self.l.append(node)
        self.match(node.left,val)
        self.match(node.right,val)
    def same(self,r1,r2):
        if not r1 and not r2:
            return True
        if r1 and r2 and r1.val!=r2.val:
            return False
        if r1 and not r2 or not r1 and r2:
            return False
        return self.same(r1.left,r2.left) and self.same(r1.right,r2.right)