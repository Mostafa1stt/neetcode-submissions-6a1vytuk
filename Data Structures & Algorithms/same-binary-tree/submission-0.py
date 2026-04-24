# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def compare(self,root,aroot):
        if root is aroot:
            return True
        if not root or not aroot:
            return False
        if root.val != aroot.val:
            return False
        else:
            return min(self.compare(root.left,aroot.left),self.compare(root.right,aroot.right))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p,q)
        