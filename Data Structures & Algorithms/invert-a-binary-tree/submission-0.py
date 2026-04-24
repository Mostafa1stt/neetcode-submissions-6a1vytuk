# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invert(self, root):
        if root is None:
            return 
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invert(root.right)
        self.invert(root.left)

    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lol = root
        self.invert(root)
        return lol