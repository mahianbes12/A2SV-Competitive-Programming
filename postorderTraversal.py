# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L=[]
        def pot(node):
            if node is None:
                return
            pot(node.left)
            pot(node.right)
            L.append(node.val)
            return L
        return pot(root)
