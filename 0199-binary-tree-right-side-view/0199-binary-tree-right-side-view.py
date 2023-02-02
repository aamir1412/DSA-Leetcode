# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            count = len(q)
            for i in range(len(q)):                                    
                n = q.popleft()
                count -= 1                
                if count == 0:
                    res.append(n.val)                    
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)                
        return res
                
                    