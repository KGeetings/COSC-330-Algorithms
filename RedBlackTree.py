class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 'black')
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = Node(key, 'red', self.NIL_LEAF, self.NIL_LEAF)
        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = 'black'
        else:
            self._insert_recursive(self.root, new_node)
        self.inorder_traversal(self.root)
        print()

    def _insert_recursive(self, current, new_node):
        if new_node.key < current.key:
            if current.left == self.NIL_LEAF:
                current.left = new_node
                new_node.parent = current
                self._insert_fixup(new_node)
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right == self.NIL_LEAF:
                current.right = new_node
                new_node.parent = current
                self._insert_fixup(new_node)
            else:
                self._insert_recursive(current.right, new_node)

    def _insert_fixup(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    if node.parent:
                        node.parent.color = 'black'
                    if node.parent and node.parent.parent:
                        node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    if node.parent:
                        node.parent.color = 'black'
                    if node.parent and node.parent.parent:
                        node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'black'

    """ def inorder_traversal(self, node):
        if node != self.NIL_LEAF:
            self.inorder_traversal(node.left)
            print(f"Key: {node.key}, Color: {node.color}")
            self.inorder_traversal(node.right) """
    
    def inorder_traversal(self, node):
        if node != self.NIL_LEAF:
            self.inorder_traversal(node.left)
            print(node.key, end=', ')  # Print keys in one line separated by commas
            self.inorder_traversal(node.right)

    def _left_rotate(self, node):
        if node is None or node.right is None:
            return

        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        if node:
            node.parent = right_child

    def _right_rotate(self, node):
        if node is None or node.left is None:
            return

        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        if node:
            node.parent = left_child

def main():
    tree1 = RedBlackTree()
    keys1 = [41, 38, 31, 12, 19, 8]
    print("Inserting keys into Tree 1:")
    for key in keys1:
        tree1.insert(key)

    tree2 = RedBlackTree()
    keys2 = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    print("\n\nInserting keys into Tree 2:")
    for key in keys2:
        tree2.insert(key)

if __name__ == "__main__":
    main()
