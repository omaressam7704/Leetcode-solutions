class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True  # An empty tree is considered a valid binary tree

        # Recursively check if the left and right subtrees are valid
        left_valid = self.checkTree(root.left)
        right_valid = self.checkTree(root.right)

        # Check if the current node's value satisfies the condition
        current_valid = (root.left.val + root.right.val == root.val) if (root.left and root.right) else True

        # Return True only if all conditions are satisfied
        return left_valid and right_valid and current_valid
