# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcounter(self,root,counter):
        if root is None:
            return counter
        counter += 1
        return max(self.lcounter(root.right,counter),self.lcounter(root.left,counter))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.lcounter(root,0)
        