# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True


        def dfs(pNode, qNode):
            if not pNode and not qNode:
                return
            if not pNode or not qNode:
                self.same = False
                return
            
            if pNode.val != qNode.val:
                self.same = False
                return
            
            dfs(pNode.left, qNode.left)
            dfs(pNode.right, qNode.right)

        dfs(p, q)

        return self.same
                