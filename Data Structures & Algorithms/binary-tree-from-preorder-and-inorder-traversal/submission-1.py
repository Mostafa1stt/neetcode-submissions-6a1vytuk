# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildt(self,preorder, inorder):
        if not inorder:
            return None
        val = preorder.pop(0)
        node = TreeNode(val)
        leftl = []
        rightl = []
        found = False
        for i in inorder:
            if i == val:
                found = True
                continue
            if found :
                rightl.append(i)
            else:
                leftl.append(i)
        node.left = self.buildt(preorder,leftl)
        node.right = self.buildt(preorder,rightl)
        return node 
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildt(preorder,inorder)
            
        
            
