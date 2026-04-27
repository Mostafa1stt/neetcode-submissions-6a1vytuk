# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smalll(self,root,lists):
        if root is None:
            return lists
        self.smalll(root.right,lists)
        lists.append(root.val)
        self.smalll(root.left,lists)
        return lists
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
       return self.smalll(root,[])[-k]
        