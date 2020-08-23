# 미해결

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


t1 = TreeNode(1)
# t1 = TreeNode{1, left: TreeNode{val: 3, left: TreeNode{val: 5, left: None, right: None}, right: None}, right: TreeNode{val: 2, left: None, right: None}}
# t2 = TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: TreeNode{val: 4, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 7, left: None, right: None}}}
print(t1)

# class Tree(object):
#     def __init__(self, data, left_child=None, right_child=None):
#         self.data = data
#         self.left_child = left_child
#         self.right_child = right_child


# parent = Tree(1, Tree(3), Tree(4))


# def init_tree():
#     # create leaf node
#     leaf = []
#     for i in range(6):
#         leaf.append(Tree(i+1))

#     # create sub tree
#     left_subtree = Tree(
#         9, Tree(7, leaf[0], leaf[1]), Tree(8, leaf[2], leaf[3]))
#     right_subtree = Tree(10, leaf[4], leaf[5])

#     root = Tree(11, left_subtree, right_subtree)
#     return root


# print(init_tree())
