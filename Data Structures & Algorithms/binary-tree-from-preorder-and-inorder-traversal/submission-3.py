class Solution:
    def buildt(self, preorder, inorder):
        if not inorder:
            return None
        
        val = preorder.pop(0)
        node = TreeNode(val)
        mid = inorder.index(val)  # finds split point directly
        
        node.left = self.buildt(preorder, inorder[:mid])
        node.right = self.buildt(preorder, inorder[mid+1:])
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildt(preorder, inorder)