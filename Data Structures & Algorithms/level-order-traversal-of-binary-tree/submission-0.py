# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leveler(self,root,lists,level):
        if root == None:
            return lists
        if not(level in  lists):
            lists[level] = [root.val]
        else:
            lists[level].append(root.val)
        self.leveler(root.left,lists,level+1)
        self.leveler(root.right,lists,level+1)
        return list(lists.values())
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        return self.leveler(root,dict(),0)