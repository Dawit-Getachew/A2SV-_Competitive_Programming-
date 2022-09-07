# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        data = ""
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is None:
                data += "#,"
            else:
                data += str(node.val) + ","
                if node is not None:
                    queue.append(node.left)
                    queue.append(node.right)
        return data
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
			
        data_arr = data.split(",")
        root = TreeNode(data_arr.pop(0))
        queue = [root]
        while queue:
            node = queue.pop(0)
            str1 = data_arr.pop(0)
            if str1 == "#":
                node.left = None
            else:
                node.left = TreeNode(str1)
                queue.append(node.left)
            str2 = data_arr.pop(0)
            if str2 == "#":
                node.right = None
            else:
                node.right = TreeNode(str2)
                queue.append(node.right)
        return root        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans