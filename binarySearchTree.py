class Node:
    """
    Tree node: left and right child + data
               which can be any object
    """
    def __init__(self, data):
        """
        Node constructor
        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        @param data node data object to look up
        @param parent node’s parent
        @returns node and node’s parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        """
        Returns the number of children
        @returns number of children: 0, 1, 2
        """
        if self is None:
            return None
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        """
        Delete node containing data
        @param data node’s content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()

        if children_count == 0:
            # if node has no children, just remove it
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            del node

        elif children_count == 1:
            # if node has 1 child
            # replace node by its child
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
            del node

        else:
            # if node has 2 children
            # find its successor
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            # replace node data by its successor data
            node.data = successor.data
            # fix successor’s parent’s child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def in_order(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        """
        Print tree content preorder
        """
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        """
        Print tree content postorder
        """
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)

testA = Node(8)
testA.insert(4)
testA.insert(2)
testA.insert(1)
testA.insert(3)
testA.insert(6)
testA.insert(5)
testA.insert(7)
testA.insert(12)
testA.insert(10)
testA.insert(9)
testA.insert(11)
testA.insert(14)
testA.insert(13)
testA.insert(15)
testB = Node(8)
testB.insert(4)
testB.insert(2)
testB.insert(1)
testB.insert(3)
testB.insert(6)
testB.insert(5)
testB.insert(7)
testB.insert(12)
testB.insert(10)
testB.insert(9)
testB.insert(11)
testB.insert(14)
testB.insert(13)
testB.insert(15)

testA.delete(8)
testA.in_order()

#testA.pre_order()
#testB.pre_order()
testA.delete(4)
testA.delete(6)

testB.delete(6)
testB.delete(4)

#testA.post_order()
#testB.post_order()

#testA.pre_order()
#testB.pre_order()

'''
root = Node(8)

root.insert(3)
root.insert(10)
root.insert(1)

root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

node, parent = root.lookup(7)
node, parent = root.lookup(15)

root.delete(1)

root.delete(14)

root.delete(3)

root.print_tree()
'''
