class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:  #根節點 = 空(none)
            self.root = TreeNode(value)
            return
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:  #左
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:  #右
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

print()
bst = BSTL()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
print(bst.inorder_traversal(bst.root))
