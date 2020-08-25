class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]


# 초기 풀이
# class Solution:

#     def maxLength(self, root):
#         if not root:
#             return 0

#         leftLength = self.maxLength(root.left)
#         rightLength = self.maxLength(root.right)

#         return max(leftLength, rightLength)+1

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         else:
#             leftLength = self.maxLength(root.left)  # 1
#             rightLength = self.maxLength(root.right)  # 6
#             print(leftLength, rightLength)
#             return leftLength + rightLength

# 답안
# class Solution():
#     def diameterOfBinaryTree(self, root):
#         ans = 1

#         def depth(node):
#             if not node:
#                 return 0
#             L = depth(node.left)
#             R = depth(node.right)
#             nonlocal ans
#             ans = max(ans, L+R+1)
#             return max(L, R) + 1

#         depth(root)
#         return ans - 1


# 내 풀이
class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0

        def maxLength(root):
            if not root:
                return 0

            leftLength = maxLength(root.left)
            rightLength = maxLength(root.right)
            nonlocal ans
            # 각 root를 훑을 때 그 root의 최대 길이 구하기
            ans = max(ans, leftLength + rightLength)

            return max(leftLength, rightLength) + 1  # 훑고 있는 root의 최대 깊이 구하기
        maxLength(root)

        return ans
