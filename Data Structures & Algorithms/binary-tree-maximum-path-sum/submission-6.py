class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # get max gain from left and right (ignore negatives)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # path passing through this node
            current_sum = node.val + left + right

            # update global maximum
            self.max_sum = max(self.max_sum, current_sum)

            # return best single path to parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum