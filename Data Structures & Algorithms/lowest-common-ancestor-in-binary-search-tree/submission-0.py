# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.p1=[]
        self.p2=set()

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.traverse(root,1,p)
        self.traverse(root,2,q)
        for x in self.p1[::-1]:
            if x in self.p2:
                return x
    
    def  traverse(self,node,no,target):
        if no==1:
            self.p1.append(node)
        else:
            self.p2.add(node)
        if node.val==target.val:
            return
        elif target.val<node.val:
            return self.traverse(node.left,no,target)
        else:
            return self.traverse(node.right,no,target)
