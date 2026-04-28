class Solution:
    def buildt(self, preorder, inorder, idx):
        if not inorder:
            return None
        
        val = preorder[idx[0]]
        idx[0] += 1
        node = TreeNode(val)
        mid = inorder.index(val)
        
        node.left = self.buildt(preorder, inorder[:mid], idx)
        node.right = self.buildt(preorder, inorder[mid+1:], idx)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildt(preorder, inorder, [0])