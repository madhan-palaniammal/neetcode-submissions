# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidHelper(
            root,
            -1001,
            1001
        )

    def isValidHelper(self, root, min_val, max_val):
        if not root:
            return True

        if root.left and (not root.left.val < root.val or not root.left.val > min_val):
            return False

        if root.right and (not root.right.val > root.val or not root.right.val < max_val):
            return False

        res = (
            self.isValidHelper(
                root.left, 
                min_val,
                root.val
            ) and
            self.isValidHelper(
                root.right,
                root.val,
                max_val
            )
        )

        return res