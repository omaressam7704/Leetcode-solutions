class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        # Traverse the left subtree
        left_nodes = self.inorderTraversal(root.left)
        
        # Visit the current node
        current_val = root.val
        
        # Traverse the right subtree
        right_nodes = self.inorderTraversal(root.right)
        
        # Combine the results
        return left_nodes + [current_val] + right_nodes
