# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        positions = {val : i for i, val in enumerate(inorder)}

        def build(left, right):
            nonlocal preIdx
            if left > right:
                return None
            rootVal = preorder[preIdx]
            preIdx += 1
            root = TreeNode(rootVal)
            mid = positions[rootVal]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
            
        return build(0, len(preorder) - 1)
        