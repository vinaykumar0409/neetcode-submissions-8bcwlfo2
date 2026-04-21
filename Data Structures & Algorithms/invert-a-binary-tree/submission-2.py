# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """bfs"""
        # if not root:
        #     return None

        # queue = deque([root])

        # while queue:
        #     curnode = queue.popleft()

        #     curnode.left, curnode.right = curnode.right, curnode.left

        #     if curnode.left:
        #         queue.append(curnode.left)
        #     if curnode.right:
        #         queue.append(curnode.right)
        
        # return root

        """dfs"""

        def dfs(node):
            if not node:
                return None

            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)

            return node
        
        return dfs(root)



