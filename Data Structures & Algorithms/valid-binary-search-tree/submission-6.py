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
        for i in smaller:
            if root.val <= i:
                return False
        for i in bigger:
            if root.val >= i:
                return False
        new_bigger = bigger.copy()
        new_bigger.append(root.val)
        new_smaller = smaller.copy()
        new_smaller.append(root.val)
        return min(self.vailed(root.left,new_bigger,smaller),self.vailed(root.right,bigger,new_smaller))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.vailed(root,[],[])
        