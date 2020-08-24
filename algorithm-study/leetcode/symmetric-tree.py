# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sym(self, left, right):

        # 종료 조건
        if not left:
            return not right  # 왼쪽이 없는 경우 오른쪽도 없으면 True, 오른쪽이 있으면 False

        if not right:  # 왼쪽이 있는데 오른쪽이 없는 경우 False
            return False

        return left.val == right.val and self.sym(left.left, right.right) and self.sym(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.sym(root.left, root.right)
