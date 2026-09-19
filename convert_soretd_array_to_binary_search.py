# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums: return None
        middle = len(nums) // 2

        tree = TreeNode(nums[middle])

        tree.left = self.sortedArrayToBST(nums[:middle])
        tree.right = self.sortedArrayToBST(nums[middle+1:])

        return tree