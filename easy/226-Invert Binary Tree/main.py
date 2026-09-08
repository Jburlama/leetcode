from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root

def create_tree(nums: List, i=0) -> Optional[TreeNode]:
    if i >= len(nums):
        return None

    root = TreeNode(nums[i])
    root.left = create_tree(nums, i * 2 + 1)
    root.right = create_tree(nums, i * 2 + 2)
    return root
    
    

def print_tree(root: Optional[TreeNode]) -> None:
    if not root:
        return None
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


root = [4,2,7,1,3,6,9]
root_head = create_tree(root)

print_tree(root_head)
print()
s = Solution()
print_tree(s.invertTree(root_head))
