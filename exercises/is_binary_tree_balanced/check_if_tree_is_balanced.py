class Node():
    def __init__(self, value, left_node = None, right_node = None):
        self.left_node = left_node
        self.right_node = right_node
        self.value = value

    def set_left(self,node):
        self.left_node = node

    def set_right(self,node):
        self.right_node = node



def is_tree_balanced(root):

    print("at node ", root.value)
    if not root.left_node and not root.right_node:
        #we are at leaf node
        print("leaf node", "return 1")
        return 1

    left_height = 0
    if root.left_node:
        left_height = is_tree_balanced(root.left_node)
        if left_height == -1:
            print("left return -1")
            return -1
    right_height = 0
    if root.right_node:
        right_height = is_tree_balanced(root.right_node)
        if right_height == -1:
            print("right return -1")
            return -1

    if abs(left_height - right_height) > 1:
        print("imbalance return -1")
        return -1
    else:
        print("return max of ", left_height, right_height)
        return max(left_height + 1, right_height +1)

    return res

if __name__ == '__main__':
    """
    tree like:
    5------
    |      |
    3-     8--
    | |    |  |
    2 4    7  9--
    |            |
    1            10
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node5.set_left(node3)
    node5.set_right(node8)
    node3.set_left(node2)
    node3.set_right(node4)
    node2.set_left(node1)
    node8.set_left(node7)
    node8.set_right(node9)
    node9.set_right(node10)

    print(is_tree_balanced(node5))


    """
    unbalanced tree like:
    5------
    |      |
    3-     8--
    | |    |  |
    2 4    7  9--
    |            |
    1            10
                 |
                 11
                 |
                 12
    """
    node11 = Node(11)
    node12 = Node(12)
    node10.set_left(node11)
    node11.set_left(node12)
    print(is_tree_balanced(node5))


