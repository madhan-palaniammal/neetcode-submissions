# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        stack.append(root)
        
        while stack:
            r = stack.pop()
            if self.isSameTree(r, subRoot):
                return True
    
            if r:
                stack.append(r.left)
                stack.append(r.right)

        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and not q) or (not p and q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)