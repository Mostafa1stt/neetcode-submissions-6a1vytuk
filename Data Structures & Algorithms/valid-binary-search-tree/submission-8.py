# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def vailed(self,root,bigger,smaller):
        if root is None:
            return True
        if root.val >= bigger or root.val <= smaller:
            return False
        new_bigger = root.val
        new_smaller = root.val
        return min(self.vailed(root.left,new_bigger,smaller),self.vailed(root.right,bigger,new_smaller))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.vailed(root,float("inf"),float("-inf"))
        