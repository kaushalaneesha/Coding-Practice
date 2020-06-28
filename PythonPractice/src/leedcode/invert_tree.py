"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Input :
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a
whiteboard so f*** off.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        print(self.val)
        if self.left: self.left.print()
        if self.right: self.right.print()


def create_tree_node(arr):
    if not arr:
        return
    if arr[0] is None:
        print("Root node cant be null")
        return
    return create_tree_util(arr, 0)


def create_tree_util(arr, index):
    if index >= len(arr):
        return None
    if not arr[index]:
        return create_tree_util(arr, index+1)
    new_node = TreeNode(arr[index], create_tree_util(arr, 2 * index + 1), create_tree_util(arr, 2 * index + 2))
    return new_node


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)
        root.left = inverted_right
        root.right = inverted_left
        return root


# Test
arr = [4, 2, None, 1, 3, 6, 9]
t = create_tree_node(arr)
print(t.left.left.left.val)

# s = Solution()
# inverted_root = s.invertTree(t)
# inverted_root.print()
