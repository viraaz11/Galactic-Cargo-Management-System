from node import Node

class AVLTree:
    def __init__(self, compare_function):
        self.node: Node = None
        self.size = 0
        self.comparator = compare_function

    def get_height(self, node):
        if not node: return 0
        return node.height

    def get_balance(self, node):
        if not node: return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, key, value):

        new_node = Node(key, value)
        self.node = self._insert(self.node, new_node)
        self.size += 1
        return self.node

    def _insert(self, node, new_node):
        if not node: return new_node
        comparison = self.comparator(new_node, node)
        if comparison < 0: node.left = self._insert(node.left, new_node)
        elif comparison > 0: node.right = self._insert(node.right, new_node)
        else: return 
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and self.comparator(new_node, node.left) < 0:
            return self.right_rotate(node)
        if balance < -1 and self.comparator(new_node, node.right) > 0:
            return self.left_rotate(node)
        if balance > 1 and self.comparator(new_node, node.left) > 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.comparator(new_node, node.right) < 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def delete(self, element):
        self.node = self.delete_node(self.node, element)
        if self.node: self.size -= 1
        return self.node
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left

        return current

    def delete_node(self,root: Node, key: Node):
        
        if root is None:
            return root

        comparison = self.comparator(key, root)
        if comparison<0:
            root.left = self.delete_node(root.left, key)

        elif comparison>0:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right
                if temp is None:
                    root = None
                else:  
                    root = temp

            else:
                temp = self.min_value_node(root.right)
                root.key = temp.key
                root.value=temp.value
                root.right = self.delete_node(root.right, temp)
        if root is None:
            return root

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    

    def find(self, key):
        return self._find(self.node, key)

    def _find(self, node, element):
        if not node or node.key == element:
            return node.value if node else None
        if element < node.key:
            return self._find(node.left, element)
        return self._find(node.right, element)
    
    def inorder(self):
        ans=[]
        def traverse(root,ans):
            if not root: return
            traverse(root.left,ans)
            ans.append(root.key)
            traverse(root.right,ans)
        traverse(self.node,ans)
        return ans